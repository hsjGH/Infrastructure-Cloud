import sqlite3
import hashlib
from flask import Flask, request, render_template_string, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Nodig voor flash messages

db_name = 'test.db'

# HTML templates als strings
INDEX_HTML = """
<h2>Welcome to the Python Login App</h2>
<p><a href="/signup">Signup</a> | <a href="/login">Login</a></p>
"""

SIGNUP_HTML = """
<h2>Signup</h2>
<form method="POST">
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    <input type="submit" value="Signup">
</form>
<p>{{ message }}</p>
<p><a href="/">Back</a></p>
"""

LOGIN_HTML = """
<h2>Login</h2>
<form method="POST">
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    <input type="submit" value="Login">
</form>
<p>{{ message }}</p>
<p><a href="/">Back</a></p>
"""

# --- Functies voor database ---
def create_tables():
    """Maak de tabellen aan als ze nog niet bestaan"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    # Plain text tabel
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN (
        USERNAME TEXT PRIMARY KEY NOT NULL,
        PASSWORD TEXT NOT NULL
    );''')
    # Hash tabel
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH (
        USERNAME TEXT PRIMARY KEY NOT NULL,
        HASH TEXT NOT NULL
    );''')
    conn.commit()
    conn.close()

def add_user_plain(username, password):
    """Voeg een gebruiker toe in plain text"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def add_user_hash(username, password):
    """Voeg een gebruiker toe met SHA256 hash"""
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) VALUES (?, ?)", (username, hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def verify_plain(username, password):
    """Verifieer plain text login"""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = ?", (username,))
    record = c.fetchone()
    conn.close()
    if not record:
        return False
    return record[0] == password

def verify_hash(username, password):
    """Verifieer hash login"""
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT HASH FROM USER_HASH WHERE USERNAME = ?", (username,))
    record = c.fetchone()
    conn.close()
    if not record:
        return False
    return record[0] == hash_value

# --- Routes ---
@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Kies hier: plaintext of hash
        if add_user_hash(username, password):
            message = 'Signup success (hashed password)'
        else:
            message = 'Username already exists'
    return render_template_string(SIGNUP_HTML, message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Kies hier: plain of hash verificatie
        if verify_hash(username, password):
            message = f'Login success! Welcome {username}'
        else:
            message = 'Invalid username/password'
    return render_template_string(LOGIN_HTML, message=message)

if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
