import json
from interfaces import Base, Residential
from typing import List

def get_buildings_data(file_address: str):
    with open(file_address, 'r') as file:
        geojson_data = json.load(file)

    features_list = []

    for feature in geojson_data["features"]:
        properties = feature["properties"]
        coordinates = feature["geometry"]["coordinates"][0]

        center_x = sum(coord[0] for coord in coordinates) / len(coordinates)
        center_y = sum(coord[1] for coord in coordinates) / len(coordinates)

        base_metadata = Base(
            roadDistance=0,
            residentialDistance=0,
            hospitalDistance=0,
            agriculturalDistance=0,
            commercialDistance=0,
            industrialDistance=0,
            schoolDistance=0,
            healthDistance=0,
            sewageTreatmentDistance=0,
            waterBodyDistance=0
        )

        residential_building = Residential(
            key=str(properties["OBJECTID"]),
            type="RESIDENTIAL",
            floors=properties.get("No_Floors", 1),
            boundaryPoints=coordinates,
            centralPoint=[center_x, center_y],
            metadata=base_metadata
        )

        features_list.append(residential_building.to_dict())

    return features_list
