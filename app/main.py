from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps application is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/info")
def info():
    return jsonify({
        "application": "DevOps Demo Application",
        "version": "1.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)