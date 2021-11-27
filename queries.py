import sqlite3
import time
DATABASE = 'inno.db'

def borrow(code):
    '''sql = "INSERT INTO btable (code) VALUES (?)"
    values = (code,)'''

    sql = "SELECT sno FROM user WHERE code = (?)"
    values = (code,)
    sno = execute_(sql, values)
    sno = sno[0]

    sql = "SELECT name FROM user WHERE code = (?)"
    values = (code,)
    name = execute_(sql, values)
    name = name[0]

    now_time = time.time()
    tm = time.localtime(now_time)
    time_string = time.strftime('%Y-%m-%d %H:%M:%S ', tm)

    sql = "INSERT INTO btable (code, name, sno, time) VALUES (?, ?, ?, ?)"
    values = (code, name, sno, time_string)
    execute(sql, values)


def retum(code):
    sql = "UPDATE btable SET returned = 1 WHERE code = ? AND returned = 0"
    values = (code,)
    execute(sql, values)

def adduser(name, sno, code, time_string):
    sql = "INSERT INTO user (name, sno, code, time) VALUES (?, ?, ?, ?)"
    values = (name, sno, code, time_string)
    execute(sql, values)


def is_dup_sno(sno):
    sql = "SELECT * FROM user WHERE sno = ?"
    values = (sno,)

    return execute_bool(sql, values)

def is_dup_eq(code):
    sql = "SELECT * FROM equipment WHERE code = ?"
    values = (code,)

    return execute_bool(sql, values)

def is_code_match(code):
    sql = "SELECT * FROM user WHERE code = ?"
    values = (code,)
    return execute_bool(sql, values)


def qr_to_eqname(code):
    sql = "SELECT name FROM equipment WHERE cod = ?"

    return execute_to()

def execute_(sql, values):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(sql, values)
    result = c.fetchone()
    conn.close()

    return result

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