from flask import Flask, render_template
import queries as q

app = Flask(__name__)

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
