from flask import Flask, render_template, redirect, url_for, request

import queries as q
import time

app = Flask(__name__)
warn = 0

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/slist')
def slist():
    return render_template('slist.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/bsqr')
def bsqr():
    result = request.form
    return render_template('bsqr.html', result=result)

@app.route('/bdone', methods=['POST'])
def bdone():
    result = request.form
    print(result)

    if not q.is_code_match(result['code'][:32]):
        return render_template('warning.html', message="등록된 QR코드와 일치하지 않습니다.")

    #q.borrow(result['sno'], result['code'], result['image'], result['ddate'])
    q.borrow(result['code'][:32],)
    return render_template('bdone.html')

@app.route('/pluss')
def pluss():
    return render_template('pluss.html')

@app.route('/bdon', methods=['POST'])
def bdon():
    return redirect(url_for('main'))

@app.route('/psdone', methods=['POST'])
def psdone():
    now_time = time.time()
    tm = time.localtime(now_time)
    time_string = time.strftime('%Y-%m-%d %H:%M:%S ', tm)

    result = request.form
    q.adduser(result['name'], result['sno'], result['code'][:32], time_string)
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
