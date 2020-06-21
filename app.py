from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'inno.db'

def get_conn():
    return sqlite3.connect(DATABASE)

def init_conn():
    conn = get_conn()
    c = conn.cursor()
    #sql = "CREATE TABLE equipment (name varchar(100), code varchar(100))"
    #sql = "CREATE TABLE btable (sno VARCHAR(8), code VARCHAR(8), image BLOB, bdate DATE, ddate DATE)"
    sql = "INSERT INTO equipment VALUES ('아이패드', '18022300190001')"
    c.execute(sql)
    conn.commit()
    conn.close()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/bsnum')
def bsnum():
    return render_template('bsnum.html')

@app.route('/bsqr')
def bsqr():
    return render_template('bsqr.html')

@app.route('/beqr')
def beqr():
    return render_template('beqr.html')

@app.route('/beimage')
def beimage():
    return render_template('beimage.html')

@app.route('/bcal')
def bcal():
    return render_template('bcal.html')

@app.route('/bdone')
def bdone():
    return render_template('bdone.html')

@app.route('/pluse')
def pluse():
    return render_template('pluse.html')

@app.route('/pluss')
def pluss():
    return render_template('pluss.html')

@app.route('/rdone')
def rdone():
    return render_template('rdone.html')

@app.route('/reimage')
def reimage():
    return render_template('reimage.html')

@app.route('/reqr')
def reqr():
    return render_template('reqr.html')


if __name__ == '__main__':
    app.run(debug=False)
    #init_conn()
