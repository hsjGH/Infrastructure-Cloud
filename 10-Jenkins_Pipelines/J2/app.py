# Importeer Flask en render_template om HTML te tonen
from flask import Flask, render_template
# Importeer datetime om de huidige tijd te tonen
from datetime import datetime

# Maak een Flask-app object
app = Flask(__name__)

# Definieer de hoofdpagina
@app.route("/")
def home():
    # Haal de huidige datum en tijd op
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Render de HTML-template en geef de tijd mee
    return render_template("index.html", current_time=now)

# Start de Flask-app wanneer dit script direct wordt uitgevoerd
if __name__ == "__main__":
    # Luister op alle interfaces, poort 5000
    app.run(host="0.0.0.0", port=5000)
