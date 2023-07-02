from flask import Flask, jsonify, request
import os
os.environ["MY_ENVIRONMENT_VARIABLE"] = "50"

app = Flask(__name__)

def get_environment_variable():
    variable_name = "MY_ENVIRONMENT_VARIABLE"
    value = os.environ.get(variable_name)
    return value

@app.route("/get_variable", methods=["GET"])
def get_variable():
    variable_value = get_environment_variable()
    if variable_value is not None:
        return jsonify({"variable": variable_value})
    else:
        return jsonify({"error": "Environment variable not found"}), 500
    
@app.route("/healthy", methods=["GET"])
def healthy():
    return jsonify({"status": "ok"})

@app.route('/edit_variable', methods=["POST"])
def edit_variable():
    title = request.json['title']
    content = request.json['content']

    return jsonify({"message": "environment variable is changed"})

if __name__ == "__main__":
    app.run()

