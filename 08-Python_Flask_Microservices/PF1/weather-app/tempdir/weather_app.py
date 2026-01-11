from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(lat, lon):
    try:
        r = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",
            timeout=5
        ).json()
        return r.get("current_weather", {})
    except:
        return {}

@app.route("/")
def main():
    # Dynamische locatie via query parameters van de client
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    # fallback als geen locatie meegegeven
    if lat is None or lon is None:
        lat = 0.0
        lon = 0.0
    else:
        lat = float(lat)
        lon = float(lon)

    weather = get_weather(lat, lon)

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
