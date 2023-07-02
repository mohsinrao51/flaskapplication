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

@app.route("/edit_variable", methods=["POST"])
def edit_variable():
    new_value = request.json.get("value")
    if new_value is not None:
        os.environ[variable_name] = new_value
        return jsonify({"message": "Environment variable updated successfully"})
    else:
        return jsonify({"error": "Invalid request data"}), 400



if __name__ == "__main__":
    app.run()

