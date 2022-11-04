from flask import Flask
import os

app = Flask(__name__)
count=0


@app.route("/health")
def health():
    #return str(os.environ.get("STATUS"))
    return "OK"

@app.route("/counter")
def counter1():
    global count
    count += 1
    return str(count)

@app.route("/")
def hello_world():
    return "olá mundo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("APP_PORT"), debug=True)
