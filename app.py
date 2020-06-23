from flask import Flask, render_template, redirect, url_for, request
import queries as q

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/bsnum')
def bsnum():
    return render_template('bsnum.html')

@app.route('/bsqr', methods=['POST'])
def bsqr():
    result = request.form
    return render_template('bsqr.html', result=result)

@app.route('/beqr', methods=['POST'])
def beqr():
    result = request.form
    return render_template('beqr.html', result=result)

@app.route('/beimage', methods=['POST'])
def beimage():
    result = request.form
    return render_template('beimage.html', result=result)

@app.route('/bcal', methods=['POST'])
def bcal():
    result = request.form
    return render_template('bcal.html', result=result)

@app.route('/bdone', methods=['POST'])
def bdone():
    result = request.form
    print(result)
    #q.borrow(result['sno'], result['code'], result['image'], result['ddate'])
    q.borrow(result['sno'], result['code'], None, result['ddate'])
    return render_template('bdone.html', ddate=result['ddate'], name='아이패드')

@app.route('/pluse')
def pluse():
    return render_template('pluse.html')

@app.route('/pluss')
def pluss():
    return render_template('pluss.html')

@app.route('/rdone', methods=['POST'])
def rdone():
    result = request.form
    print(result)
    q.retum(result['code'])
    return render_template('rdone.html')

@app.route('/reimage', methods=['POST'])
def reimage():
    result = request.form
    return render_template('reimage.html', result=result)

@app.route('/reqr')
def reqr():
    return render_template('reqr.html')

@app.route('/rdon', methods=['POST'])
def rdon():
    return redirect(url_for('main'))

@app.route('/bdon', methods=['POST'])
def bdon():
    return redirect(url_for('main'))

@app.route('/psdone', methods=['POST'])
def psdone():
    result = request.form
    q.adduser(result['name'], result['sno'], result['code'][:32])
    return redirect(url_for('main'))

@app.route('/pedone', methods=['POST'])
def pedone():
    result = request.form
    q.addeq(result['name'], result['code'][:32])
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
