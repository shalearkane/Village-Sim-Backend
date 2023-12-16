import json

from flask import Flask
from services.get_buildings_data import get_buildings_data

app = Flask(__name__)

@app.route("/residential")
def residential_data():
    residential_data = get_buildings_data('data/Builtup_Kalonda.geojson')
    return json.dumps(residential_data)