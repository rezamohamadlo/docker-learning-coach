FROM python:3.12-slim
WORKDIR /app
RUN groupadd --gid 10001 learner && useradd --uid 10001 --gid 10001 --no-create-home learner && mkdir /data && chown 10001:10001 /data
COPY --chown=10001:10001 app.py /app/app.py
USER 10001:10001
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["python", "app.py"]
