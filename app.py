from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "hello"

@app.route('/')
def htmlfile():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)