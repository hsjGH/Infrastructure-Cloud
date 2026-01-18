# Import Flask en modules voor request, templates, sqlite en hashfuncties
from flask import Flask, request, render_template
import sqlite3
import hashlib

# Initialiseer Flask applicatie
microweb_app = Flask(__name__)

# Databasebestand
db_name = 'user.db'

# -------- DELETE ALL RECORDS ----------
@microweb_app.route('/delete/all', methods=['POST', 'DELETE'])
def delete_all():
    # Open database verbinding
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    # Verwijder alle records uit USER_PLAIN
    sql_statement = "DELETE FROM USER_PLAIN ; "
    c.execute(sql_statement)
    # Verwijder alle records uit USER_HASH
    sql_statement = "DELETE FROM USER_HASH ; "
    c.execute(sql_statement)
    db_conn.commit()
    db_conn.close()
    # Terugkoppeling
    return "Test records deleted\n"

# -------- SIGNUP PLAIN TEXT ----------
@microweb_app.route('/signup/plain', methods=['POST'])
def signup_v1():
    # Open database verbinding
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    # Creëer tabel USER_PLAIN indien niet aanwezig
    sql_statement = "CREATE TABLE IF NOT EXISTS USER_PLAIN (USERNAME TEXT PRIMARY KEY NOT NULL, PASSWORD TEXT NOT NULL); "
    c.execute(sql_statement)
    db_conn.commit()
    try:
        # Voeg gebruiker toe met username en password uit formulier
        sql_statement = "INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES ('{0}' , '{1}')".format(request.form['username'] , request.form['password'])
        c.execute(sql_statement)
        db_conn.commit()
    except sqlite3.IntegrityError:
        # Foutmelding bij bestaande username
        return "Username has been registered, but is insecure\n"
    return "Signup success, but insecure\n"

def verify_plain(username, password):
    # Haal password op uit database voor opgegeven username
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(username)
    c.execute(sql_query)
    records = c.fetchone()
    db_conn.close()
    if not records:
        return False
    # Vergelijk opgeslagen password met opgegeven password
    return records[0] == password

@microweb_app.route('/login/plain', methods=['GET', 'POST'])
def login_v1():
    error = None
    if request.method == 'POST':
        if verify_plain(request.form['username'], request.form['password']):
            error = 'Login success, but insecure\n'
        else:
            error = 'Invalid username/password\n'
    else:   
        error = 'Invalid Method\n'
    return error

# -------- SIGNUP HASH ----------
@microweb_app.route('/signup/hash', methods=['POST'])
def signup_v2():
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    # Creëer tabel USER_HASH indien niet aanwezig
    sql_statement = "CREATE TABLE IF NOT EXISTS USER_HASH (USERNAME TEXT PRIMARY KEY NOT NULL, HASH TEXT NOT NULL); "
    c.execute(sql_statement)
    db_conn.commit()
    try:
        # Bereken SHA256 hash van password uit formulier
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        # Voeg gebruiker toe met hash
        sql_statement = "INSERT INTO USER_HASH VALUES ('{0}' , '{1}' ) ".format(request.form['username'], hash_value)
        c.execute(sql_statement)
        db_conn.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered\n"
    # Print username, plain password en hash (development output)
    print('username: ' , request.form['username'], ' password: ', request.form['password'], ' hash: ', hash_value)
    return "Secure signup succeeded\n"

def verify_hash(username, password):
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    # Haal hash op uit database
    sql_query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(sql_query)
    records = c.fetchone()
    db_conn.close()
    if not records:
        return False
    # Vergelijk opgegeven password na SHA256 hash met opgeslagen hash
    return records[0] == hashlib.sha256(password.encode()).hexdigest()

@microweb_app.route('/login/hash', methods=['GET', 'POST'])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'Login success, using hash\n'
        else:
            error = 'Invalid username/password\n' 
    else:
        error = 'Invalid method\n'
    return error

# -------- HOME ----------
@microweb_app.route('/')
def main():
    # Render homepagina index.html
    return render_template("index.html")

# -------- RUN SERVER ----------
if __name__ == "__main__":
    # Start server op alle interfaces, poort 5555, ssl adhoc voor development
    microweb_app.run(host="0.0.0.0", port=5555, ssl_context='adhoc')
