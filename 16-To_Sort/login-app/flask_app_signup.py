from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

db_name = "user.db"

# Zorg dat database en tabel bestaan bij starten
conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute("""                            
CREATE TABLE IF NOT EXISTS USER_HASH (
    USERNAME TEXT PRIMARY KEY,
    PASSWORD TEXT
)
    """)
conn.commit()
conn.close()

@app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():

    if request.method == 'GET':
        return render_template("signup.html")

    # POST request
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()

    try:
        username_entered = request.form.get('username')
        password_entered = request.form.get('password')

        if not username_entered or not password_entered:
            return "Missing username or password", 400

        c.execute(
            "INSERT INTO USER_HASH (USERNAME, PASSWORD) VALUES (?, ?)",
            (username_entered, password_entered)
        )
        db_conn.commit()
        return "Signup success\n"

    except sqlite3.IntegrityError:
        return "Username already exists\n"

    finally:
        db_conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

