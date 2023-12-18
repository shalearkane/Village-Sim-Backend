import uuid
import osmnx as ox
import json
import subprocess


def fetch_roads(north: float, south: float, east: float, west: float) -> dict:
    G = ox.graph_from_bbox(
        north=north, south=south, east=east, west=west, network_type="all"
    )
    Gp = ox.project_graph(G)
    Gc = ox.consolidate_intersections(
        Gp, rebuild_graph=True, tolerance=20, dead_ends=False, reconnect_edges=True
    )
    file_name = f"{north}-{south}-{east}-{west}.gpkg"
    ox.io.save_graph_geopackage(Gc, filepath=file_name)
    output = subprocess.check_output(
        [
            f'ogr2ogr -f "GeoJSON" /vsistdout/ -s_srs {Gc.graph["crs"].srs} -t_srs EPSG:4326 {file_name} edges'
        ],
        shell=True,
    )
    d: dict = json.loads(output)
    return d


def clean_roads_data(data: dict) -> dict:
    roads = {}
    for f in data["features"]:
        if f["geometry"]["type"] == "LineString":
            if type(f["properties"]["osmid"]) is str:
                roads[int(f["properties"]["osmid"])] = f["geometry"]["coordinates"]
            else:
                roads[f["properties"]["osmid"][0]] = f["geometry"]["coordinates"]

    return roads


def get_geojson_from_shapefile(prj_file: bytes, shape_file: bytes) -> dict:
    prj_filepath = f"/tmp/{uuid.uuid4()}.prj"
    shape_filepath = f"/tmp/{uuid.uuid4()}.shp"
    with open(prj_filepath, "wb") as p, open(shape_filepath, "wb") as s:
        p.write(prj_file)
        s.write(shape_file)

    output = subprocess.check_output(
        [
            f'SHAPE_RESTORE_SHX=True ogr2ogr -f "GeoJSON" /vsistdout/ -s_srs {prj_filepath} -t_srs EPSG:4326 {shape_filepath}'
        ],
        shell=True,
    )

    return json.loads(output)


if __name__ == "__main__":
    fetch_roads(28.5576, 28.5264, 77.7078, 77.6472)
    # with open("Builtup_Kalonda.prj", "rb") as p, open("Builtup_Kalonda.shp", "rb") as s:
    #     print(get_geojson_from_shapefile(p.read(), s.read()))
