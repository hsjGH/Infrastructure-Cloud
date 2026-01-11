FROM python:3.11-slim

WORKDIR /app
COPY weather_app.py .
COPY templates ./templates
RUN pip install --no-cache-dir flask requests

EXPOSE 8080
CMD ["python3", "weather_app.py"]
