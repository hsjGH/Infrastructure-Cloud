# Importeer Flask en render_template
from flask import Flask, render_template
# Importeer datetime om starttijd te tonen
from datetime import datetime

# Maak Flask-app object
app = Flask(__name__)

# Teller variabele
counter = 0

# Starttijd
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Hoofdpagina
@app.route("/")
def home():
    return f"<h1>Counter App</h1><p>Bezoek /count om te tellen!</p><p>Starttijd: {start_time}</p>"

# Teller endpoint
@app.route("/count")
def count():
    global counter
    counter += 1
    return f"<h1>Counter App</h1><p>Bezocht: {counter} keer</p>"

# Start de app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # andere poort dan sample_app.py
