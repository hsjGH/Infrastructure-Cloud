# Start vanaf een lichte Python 3.11 image
FROM python:3.11-slim

# Zet de werkdirectory in de container
WORKDIR /app

# Kopieer de dependencies lijst
COPY requirements.txt .

# Installeer Python dependencies zonder cache
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van de app (app.py + templates)
COPY . .

# Open poort 5000 in de container
EXPOSE 5000

# Start de Flask-app
CMD ["python", "app.py"]
