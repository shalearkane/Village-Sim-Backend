import uuid
import numpy as np
import osmnx as ox
import json
import subprocess

np.random.seed(0)
ox.__version__
ox.settings.use_cache = True
ox.settings.log_console = True
utn = ox.settings.useful_tags_node
oxna = ox.settings.osm_xml_node_attrs
oxnt = ox.settings.osm_xml_node_tags
utw = ox.settings.useful_tags_way
oxwa = ox.settings.osm_xml_way_attrs
oxwt = ox.settings.osm_xml_way_tags
utn = list(set(utn + oxna + oxnt))
utw = list(set(utw + oxwa + oxwt))
ox.settings.all_oneway = True
ox.settings.useful_tags_node = utn
ox.settings.useful_tags_way = utw


def get_roads(north: float, south: float, east: float, west: float) -> dict:
    G = ox.graph_from_bbox(
        north=north, south=south, east=east, west=west, network_type="all"
    )
    Gp = ox.project_graph(G)
    Gc = ox.consolidate_intersections(
        Gp, rebuild_graph=True, tolerance=20, dead_ends=False
    )
    file_name = f"{north}-{south}-{east}-{west}.osm"
    ox.io.save_graph_xml(Gc, filepath=file_name)  # type: ignore
    output = subprocess.check_output(
        [
            f'OSM_USE_CUSTOM_INDEXING=NO ogr2ogr -f "GeoJSON" /vsistdout/ {file_name} lines'
        ],
        shell=True,
    )
    d: dict = json.loads(output)
    return d


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
    # get_roads(28.5576, 28.5264, 77.7078, 77.6472)
    with open("Builtup_Kalonda.prj", "rb") as p, open(
        "Builtup_Kalonda.shp", "rb"
    ) as s:
        print(get_geojson_from_shapefile(p.read(), s.read()))
