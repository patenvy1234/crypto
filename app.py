from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def prover():
    return render_template('prover.html')

@app.route('/verifier', methods=['POST'])
def verifier():
    input_text = request.form['input']
    return redirect(url_for('success',input_text=input_text))

@app.route('/success')
def success():
    input_text = request.args.get('input_text')
    return render_template('verifier.html',input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
