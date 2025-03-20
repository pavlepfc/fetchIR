from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return redirect("http://127.0.0.1:8001")

@app.route('/resers1')
def resers():
    return redirect("http://127.0.0.1:8002")

if __name__ == '__main__':
    app.run(port=5000)