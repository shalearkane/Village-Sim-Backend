import json

from flask import Flask, request, jsonify
from services.facilities import fetch_facilities
from services.get_buildings_data import get_buildings_data
from services.get_happiness import (
    calculate_initial_happiness,
    calculate_updated_happiness_on_adding_facility,
)
from services.constants import fetch_constants, update_constants
import requests

from services.roads_shapefile import clean_roads_data, fetch_roads

app = Flask(__name__)


@app.route("/residential/kalonda")
def get_kalonda_residential_data():
    residential_data = get_buildings_data("data/Builtup_Kalonda.geojson")
    return json.dumps(residential_data)


@app.route("/facilities", methods=["GET"])
def get_facilities():
    args = request.args
    gpcode = args.get("gpcode", default=63317, type=int)
    response = requests.get(
        f"https://egramswaraj.gov.in/webservice/getGisMapAsset/{gpcode}"
    )
    return fetch_facilities(response.json())


@app.route("/roads", methods=["GET"])
def get_roads():
    args = request.args
    north = args.get("", default=28.58, type=float)
    south = args.get("", default=(north - 0.12), type=float)
    east = args.get("", default=77.72, type=float)
    west = args.get("", default=(east - 0.12), type=float)

    roads = fetch_roads(north, south, east, west)
    cleaned_roads = clean_roads_data(roads)

    return cleaned_roads


@app.route("/get_initial_happiness", methods=["POST"])
def get_initial_happiness():
    try:
        request_data = request.get_json()
        result = calculate_initial_happiness(request_data)
        return json.dumps(result)

    except Exception as e:
        return json.dumps({"error": str(e)})


@app.route("/get_updated_happiness", methods=["POST"])
def get_updated_happiness_on_adding_house():
    try:
        request_data = request.get_json()
        data = request_data["data"]
        happiness = request_data["happiness"]
        result = calculate_updated_happiness_on_adding_facility(data, happiness)
        return json.dumps(result)

    except Exception as e:
        return json.dumps({"error": str(e)})


@app.route("/constants", methods=["GET"])
def get_constants():
    constants_data = fetch_constants()
    return jsonify(constants_data)


@app.route("/constants", methods=["POST"])
def update_constants_route():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data provided"}), 400

    result = update_constants(data)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
