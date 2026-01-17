from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime

sample = Flask(__name__)

@sample.route("/")
def main():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", current_date=current_date)

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
