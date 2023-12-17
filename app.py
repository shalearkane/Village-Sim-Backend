import json

from flask import Flask, request, jsonify
from services.get_buildings_data import get_buildings_data
from services.get_happiness import get_initial_happiness, get_updated_happiness
from services.constants import get_constants, update_constants

app = Flask(__name__)

@app.route("/residential")
def residential_data():
    residential_data = get_buildings_data('data/Builtup_Kalonda.geojson')
    return json.dumps(residential_data)

@app.route("/get_initial_happiness", methods=["POST"])
def get_happiness():
    try:
        request_data = request.get_json()
        result = get_initial_happiness(request_data)
        return json.dumps(result)

    except Exception as e:
        return json.dumps({"error": str(e)})

@app.route("/get_updated_happiness", methods=["POST"])
def get_happiness():
    try:
        request_data = request.get_json()
        data = request_data["data"]
        happiness = request_data["happiness"]
        result = get_updated_happiness(data, happiness)
        return json.dumps(result)

    except Exception as e:
        return json.dumps({"error": str(e)})


@app.route("/constants", methods=["GET"])
def get_constants():
    constants_data = get_constants()
    return jsonify(constants_data)

@app.route("/constants", methods=["POST"])
def update_constants_route():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data provided"}), 400

    result = update_constants(data)
    return jsonify(result)