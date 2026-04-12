FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml /app/
COPY src /app/src
CMD ["python", "-m", "uvicorn", "dua_business.main:app", "--host", "0.0.0.0", "--port", "8080"]
