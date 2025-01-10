from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/message")
def hello_message():
    return 'This is my message for you'

if __name__ == "__main__":
    app.run(debug=True)
