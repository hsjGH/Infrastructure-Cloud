#!/bin/bash

# Lab: twee bestaande Docker-apps samen laten draaien met Docker Compose
# Zonder de apps zelf aan te passen

# Stap 1: Maak een tijdelijke directory
mkdir -p lab_multiapps
cd lab_multiapps || exit 1

# Stap 2: Kopieer bestaande apps naar deze directory
# Verwacht: sample_app.py + templates/, counter_app.py aanwezig in ../flask_lab/
mkdir -p sample_app/templates
cp ../flask_lab/sample_app.py sample_app/
cp -r ../flask_lab/templates/* sample_app/templates/

mkdir -p counter_app
cp ../flask_lab/counter_app.py counter_app/

# Stap 3: Maak Dockerfile voor sample_app
cat << 'EOF' > sample_app/Dockerfile
# Dockerfile voor bestaande sample_app
FROM python:3.11-slim
WORKDIR /app
RUN pip install flask
COPY . .
EXPOSE 8080
CMD ["python", "sample_app.py"]
EOF

# Stap 4: Maak Dockerfile voor counter_app
cat << 'EOF' > counter_app/Dockerfile
# Dockerfile voor bestaande counter_app
FROM python:3.11-slim
WORKDIR /app
RUN pip install flask
COPY . .
EXPOSE 5001
CMD ["python", "counter_app.py"]
EOF

# Stap 5: Maak Docker Compose bestand om beide containers te verbinden
cat << 'EOF' > docker-compose.yml
version: "3.9"

services:
  sample:
    build:
      context: ./sample_app
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    depends_on:
      - counter
    networks:
      - appnet

  counter:
    build:
      context: ./counter_app
      dockerfile: Dockerfile
    ports:
      - "5001:5001"
    networks:
      - appnet

networks:
  appnet:
    driver: bridge
EOF

# Stap 6: Run Docker Compose om beide containers te starten
docker-compose up --build -d

# Stap 7: Toon actieve containers
docker ps -a

# Stap 8: Test of beide apps bereikbaar zijn
echo "Test Sample App (poort 8080):"
curl -f http://localhost:8080 && echo "Sample app werkt!"

echo "Test Counter App (poort 5001):"
curl -f http://localhost:5001 && echo "Counter app werkt!"
