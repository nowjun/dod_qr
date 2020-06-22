import sqlite3

DATABASE = 'inno.db'

def borrow(sno, code, image, ddate):
    sql = "INSERT INTO btable (sno, code, image, ddate) VALUES (?, ?, ?, ?)"
    values = (sno, code, image, ddate)
    execute(sql, values)

def retum(sno, code, image, ddate):
    sql = "UPDATE btable SET returned = 1 WHERE sno = ? AND code = ? AND returned = 0"
    values = (sno, code, image, ddate)
    execute(sql, values)

def adduser(sno, code, image, ddate):
    sql = "INSERT INTO user (name, sno, code) VALUES (?, ?, ?)"
    values = (sno, code, image, ddate)
    execute(sql, values)

def addeq(sno, code, image, ddate):
    sql = "INSERT INTO equipment (name, code) VALUES (?,?)"
    values = (sno, code, image, ddate)
    execute(sql, values)

def is_dup_sno(sno):
    sql = "SELECT * FROM user WHERE sno = ?"
    values = (sno,)

    return execute_bool(sql, values)

def is_dup_eq(code):
    sql = "SELECT * FROM user WHERE code = ?"
    values = (code,)

    return execute_bool(sql, values)

def is_code_match(sno, code):
    sql = "SELECT * FROM user WHERE sno = ? AND code = ?"
    values = (sno, code)

    return execute_bool(sql, values)

def execute_bool(sql, values):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(sql, values)
    result = c.fetchone()
    conn.close()

    return result is not None

def execute(sql, values):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(sql, values)
    conn.commit()
    conn.close()