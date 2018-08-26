import sqlite3


def connect():
    conn = sqlite3.connect("employe.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employe(id INTEGER PRIMARY KEY,firstname text,lastname text,mobile INTEGER,email text,experience text,salary INTEGER,address text)")
    conn.commit()
    conn.close()


def insert(firstname, lastname, mobile, email, experience, salary, address):
    conn = sqlite3.connect("employe.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO employe VALUES(NULL,?,?,?,?,?,?,?)",
                (firstname, lastname, mobile, email, experience, salary, address))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("employe.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employe")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(firstname="", lastname="", mobile="", email="", experience="", salary="", address=""):
    conn = sqlite3.connect("employe.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM employe WHERE firstname=? OR lastname=? OR mobile=? OR email=? OR experience=? OR salary=? OR address=?",
        (firstname, lastname, mobile, email, experience, salary, address))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("employe.db")
    cur = conn.cursor()
    cur.execute("DELETE  FROM employe WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, firstname, lastname, mobile, email, experience, salary, address):
    conn = sqlite3.connect("employe.db")
    cur = conn.cursor()
    cur.execute("UPDATE employe SET firstname=?,lastname=?,mobile=?,email=?,experience=?,salary=?,address=? WHERE id=?",
                (firstname, lastname, mobile, email, experience, salary, address, id))
    conn.commit()
    conn.close()
