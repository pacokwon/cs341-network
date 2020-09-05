from flask import Flask, request
import json
import hashlib

app = Flask(__name__)


@app.route("/hello_world", methods=["GET"])
def route_hello_world():
    return json.dumps({"message": "hello world"})


@app.route("/hash", methods=["GET"])
def route_hash():
    name = request.args.get("name")
    return json.dumps({"result": hashlib.sha256(name.encode()).hexdigest()})


@app.route("/collatz", methods=["POST"])
def route_collatz():
    body = json.loads(request.data.decode("utf-8"))

    if hashlib.sha256(body["name"].encode()).hexdigest() != body["hash"]:
        response = {"error": "HASH NOT MATCHED"}
    elif not isinstance(body["number"], int):
        response = {"error": "NUMBER NOT INTEGER"}
    else:
        response = {
            "result": body["number"] // 2
            if body["number"] % 2 == 0
            else 3 * body["number"] + 1
        }

    return json.dumps(response)


if __name__ == "__main__":
    app.run()
