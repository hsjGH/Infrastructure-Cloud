#!/bin/bash
# Cleanup oude folder en aanmaken benodigde directories
rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

# ---------- Flask app ----------
cat << 'EOF' > tempdir/weather_app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(lat, lon):
    """Haalt weerdata van Open-Meteo API op."""
    try:
        r = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",
            timeout=5
        ).json()
        return r.get("current_weather", {})  # Geeft dict terug
    except:
        return {}  # Fallback bij fout

@app.route("/")
def main():
    """Hoofdroute: query params lezen, weer ophalen, template renderen"""
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if lat is None or lon is None:
        lat = 0.0
        lon = 0.0
    else:
        lat = float(lat)
        lon = float(lon)

    weather = get_weather(lat, lon)

    # Veilige dict voor template
    safe_weather = {
        "temperature": weather.get("temperature", "n.v.t."),
        "windspeed": weather.get("windspeed", "n.v.t."),
        "weathercode": weather.get("weathercode", "n.v.t."),
        "is_day": weather.get("is_day", 1),
        "time": weather.get("time", "n.v.t.")
    }
    return render_template("index.html", weather=safe_weather, lat=lat, lon=lon)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
EOF

# ---------- HTML template ----------
cat << 'EOF' > tempdir/templates/index.html
<!doctype html>
<html lang="nl">
<head>
    <meta charset="utf-8">
    <title>Weather App</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
    <style>#map { height: 300px; width: 100%; margin-top: 20px; }</style>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
    // Redirect naar URL met lat/lon query params
    if (!window.location.search.includes("lat")) {
        navigator.geolocation.getCurrentPosition(pos => {
            const lat = pos.coords.latitude;
            const lon = pos.coords.longitude;
            window.location.href = "/?lat=" + lat + "&lon=" + lon; // concatenatie ipv backticks
        }, err => {
            console.log("Locatie niet beschikbaar, default 0,0 gebruikt");
        });
    }
    </script>
</head>
<body>
    <h1>Huidig weer</h1>
    <p>Locatie: {{ lat }}, {{ lon }}</p>
    <p>Temperatuur: {{ weather.temperature }} °C</p>
    <p>Wind: {{ weather.windspeed }} km/h</p>
    <p>Weercode: {{ weather.weathercode }}</p>
    <p>Dag/nacht: {% if weather.is_day == 1 %}Dag{% else %}Nacht{% endif %}</p>
    <p>Tijd: {{ weather.time }}</p>

    <div id="map"></div>
    <script>
        const map = L.map('map').setView([{{ lat }}, {{ lon }}], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);
        L.marker([{{ lat }}, {{ lon }}]).addTo(map).bindPopup("Jouw locatie").openPopup();
    </script>
</body>
</html>
EOF

# ---------- Dockerfile ----------
cat << 'EOF' > tempdir/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY weather_app.py .
COPY templates ./templates
RUN pip install --no-cache-dir flask requests
EXPOSE 8080
CMD ["python3", "weather_app.py"]
EOF

# ---------- Build & run ----------
cd tempdir
docker rm -f weatherapp_running 2>/dev/null
docker build -t weatherapp .
docker run -d -p 8080:8080 --name weatherapp_running weatherapp
docker ps
