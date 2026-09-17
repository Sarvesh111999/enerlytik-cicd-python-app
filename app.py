from flask import Flask

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return "Enerlytik CI/CD app is running"

@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return {"result": add_numbers(a, b)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
