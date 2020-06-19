from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)
