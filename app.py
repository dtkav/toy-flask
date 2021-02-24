from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    print(request.headers)
    print(request.stream)
    print(request.stream.read())
    return jsonify({}), 200


if __name__ == "__main__":
    app.run("0.0.0.0", 8001)
