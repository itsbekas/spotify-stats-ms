from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route("/import", methods=["POST"])
def import_data():
    print(request.get_json())
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run()
