from flask import Flask, jsonify, request
from flask_cors import CORS

from chat import get_response

app = Flask(__name__)
CORS(app)


@app.route("/toxic", methods=["POST"])
def toxic_cls():
    payload = request.get_json()
    msg = payload.get("msg")
    response = get_response(msg)
    
    return jsonify({
        "answer": response
    })

if __name__ == "__main__":
    app.run("0.0.0.0", 8018)