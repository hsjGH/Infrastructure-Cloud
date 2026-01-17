#!/bin/bash

# Jenkins Lab: automatische setup van een Flask-app met Docker

# Maak een tijdelijke directory voor de lab-app
echo "Stap 1: Maak tempdir aan"
mkdir -p tempdir/templates
mkdir -p tempdir/static  # optioneel, kan later CSS/JS bevatten

# Stap 2: Maak Flask-app bestand
echo "Stap 2: Creëer app.py"
cat << 'EOF' > tempdir/app.py
# Importeer Flask en render_template voor HTML
from flask import Flask, render_template
from datetime import datetime

# Maak de Flask-app
app = Flask(__name__)

# Hoofdpagina
@app.route("/")
def home():
    # Huidige datum en tijd ophalen
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Render de template en geef tijd door
    return render_template("index.html", current_time=now)

# Start de app als script direct wordt uitgevoerd
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

# Stap 3: Maak HTML template
echo "Stap 3: Creëer index.html"
cat << 'EOF' > tempdir/templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Jenkins Lab App</title>
</head>
<body>
    <h1>Flask App via Jenkins!</h1>
    <p>Current time: {{ current_time }}</p>
</body>
</html>
EOF

# Stap 4: Maak requirements.txt
echo "Stap 4: Creëer requirements.txt"
cat << 'EOF' > tempdir/requirements.txt
flask
EOF

# Stap 5: Maak Dockerfile
echo "Stap 5: Creëer Dockerfile"
cat << 'EOF' > tempdir/Dockerfile
# Start vanaf lichte Python image
FROM python:3.11-slim

# Werkdirectory in container
WORKDIR /app

# Installeer dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de app
COPY . .

# Open poort 5000
EXPOSE 5000

# Start Flask-app
CMD ["python", "app.py"]
EOF

# Stap 6: Ga naar de tijdelijke directory
cd tempdir || exit 1

# Stap 7: Bouw Docker image
echo "Stap 6: Bouw Docker image"
docker build -t jenkinslabapp .

# Stap 8: Verwijder oude container indien aanwezig
echo "Stap 7: Stop en verwijder oude container (indien aanwezig)"
docker rm -f jenkinslabrunning 2>/dev/null || true

# Stap 9: Run nieuwe container
echo "Stap 8: Run container"
docker run -d -p 5000:5000 --name jenkinslabrunning jenkinslabapp

# Stap 10: Toon actieve containers
echo "Stap 9: Toon actieve containers"
docker ps -a

# Stap 11: Test of app bereikbaar is
echo "Stap 10: Test app via curl"
curl -f http://localhost:5000 && echo "App werkt!"
