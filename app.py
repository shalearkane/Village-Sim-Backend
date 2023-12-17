import json

from flask import Flask, request
from services.get_buildings_data import get_buildings_data
from services.get_happiness import get_initial_happiness, get_updated_happiness

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