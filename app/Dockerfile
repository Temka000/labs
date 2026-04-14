FROM python:3.11-slim
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
ENV PYTHONUNBUFFERED=1
EXPOSE 5000
CMD ["python", "app.py"]
