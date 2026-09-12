import json
import os
import socket
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def redis_command(*parts):
    payload = b"*%d\r\n" % len(parts)
    for part in parts:
        value = str(part).encode()
        payload += b"$%d\r\n" % len(value) + value + b"\r\n"
    with socket.create_connection((os.environ["REDIS_HOST"], 6379), timeout=2) as sock:
        sock.sendall(payload)
        with sock.makefile("rb") as stream:
            line = stream.readline(4096)
    if not line.endswith(b"\r\n") or line[:1] not in (b"+", b":"):
        raise RuntimeError("Unexpected Redis response")
    return line[1:-2].decode()


def count_visit():
    if os.environ.get("REDIS_HOST"):
        return int(redis_command("INCR", "dlc:visits"))
    data_dir = Path(os.environ.get("DATA_DIR", "/data"))
    data_dir.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(data_dir / "counter.sqlite") as db:
        db.execute("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, value INTEGER NOT NULL)")
        db.execute("INSERT OR IGNORE INTO counter VALUES (1, 0)")
        db.execute("UPDATE counter SET value = value + 1 WHERE id = 1")
        return db.execute("SELECT value FROM counter WHERE id = 1").fetchone()[0]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/health":
                if os.environ.get("REDIS_HOST"):
                    if redis_command("PING") != "PONG":
                        raise RuntimeError("Redis not ready")
                body, code = {"status": "ok"}, 200
            elif self.path == "/":
                body, code = {"message": os.environ.get("GREETING", "Hello Docker learner"), "visits": count_visit()}, 200
            else:
                body, code = {"error": "not found"}, 404
        except (OSError, ValueError, RuntimeError, sqlite3.Error):
            body, code = {"error": "storage unavailable"}, 503
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), Handler).serve_forever()
