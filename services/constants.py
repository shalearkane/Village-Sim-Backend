import json

CONSTANTS_FILE_PATH = "constants.json"


def update_constants(data):
    try:
        with open(CONSTANTS_FILE_PATH, "r") as file:
            existing_constants = json.load(file)

        for key, value in data.items():
            if key in existing_constants and existing_constants[key] != value:
                existing_constants[key] = value

        with open(CONSTANTS_FILE_PATH, "w") as file:
            json.dump(existing_constants, file, indent=2)

        return {"message": "Constants updated successfully"}

    except Exception as e:
        return {"error": str(e)}


def get_constants():
    try:
        with open(CONSTANTS_FILE_PATH, "r") as file:
            constants = json.load(file)

        return constants

    except FileNotFoundError:
        return {"error": "Constants file not found"}

    except Exception as e:
        return {"error": str(e)}
