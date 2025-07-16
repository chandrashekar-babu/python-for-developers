from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<h1>Hello, world</h1>"

@app.get("/about")
def about():
    return "<h1>I'm a new Pythonista!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    