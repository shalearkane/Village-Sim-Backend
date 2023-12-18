# API SPEC
CLEAN ALL API SOURCES BEFORE PUSHING TO PUBLIC GITHUB i.e. egram/grammanchitra

## Residential
**Endpoint:** `/residential`
**Method:** `GET`
**Description:** Retrieves residential data from the `Builtup_Kalonda.geojson` GeoJSON file.
**Parameters:** None

## Happiness
### Initial Happiness
**Endpoint:** `/get_initial_happiness`
**Method:** `POST`
**Description:** Calculates the initial happiness based on the provided data.
**Parameters:** JSON like object containing data for the calculation.
- Example:
```
{
    "old": {
        "houses": {
            "key:uuid": {
                "floors": 1,
                "central_point": {
                    "long": 77.56,
                    "lat": 25.61
                },
                "nearest_dist": [
                    {
                        "facility_type": "water_facility",
                        "id": "uuid",
                        "dist": 39
                    }
                ]
            }
        },
        "facilities": {
            "water_facility": {
                "key:uuid": {
                    "central_point": {
                        "long": 77.56,
                        "lat": 25.61
                    }
                }
            },
            "healthcare": {
                "key:uuid": {
                    "central_point": {
                        "long": 77.56,
                        "lat": 25.61
                    }
                }
            }
        }
    },
    "new": {
        "key": "uuid",
        "facility_type": "water_facility",
        "central_point": {
            "long": 77.56,
            "lat": 25.61
        }
    }
}
```

### Update Happiness
**Endpoint:** `/get_updated_happiness`
**Method:** `POST`
**Description:** Calculates the updated happiness based on the provided data and current happiness.
**Parameters:** JSON like object containing data for the calculation.
- Example:
```
{
  "data": {
    "old": {
      "houses": {
        "key:uuid": {
          "floors": 1,
          "central_point": {
            "long": 77.56,
            "lat": 25.61
          },
          "nearest_dist": [
            {
              "facility_type": "water_facility",
              "id": "uuid",
              "dist": 39
            }
          ]
        }
      },
      "facilities": {
        "water_facility": {
          "key:uuid": {
            "central_point": {
              "long": 77.56,
              "lat": 25.61
            }
          }
        },
        "healthcare": {
          "key:uuid": {
            "central_point": {
              "long": 77.56,
              "lat": 25.61
            }
          }
        }
      }
    },
    "new": {
      "key": "uuid",
      "facility_type": "water_facility",
      "central_point": {
        "long": 77.56,
        "lat": 25.61
      }
    }
  },
  "happiness": {
    "administrative": 0,
    "road": 0,
    "school": 0,
    "healthcare": 2,
    "haat_shop_csc": 0,
    "water_facility": 2,
    "electric_facility": 0,
    "solar_plant": 0,
    "biogas": 0,
    "windmill": 0,
    "sanitation": 0
  }
}

```


## Constants
### Get constants
**Endpoint:** `/constants`
**Method:** `GET`
**Description:** Retrieves constants data.
**Parameters:** None

### Update constants
**Endpoint:** `/constants`
**Method:** `POST`
**Description:** Updates constants data.
**Parameters:** JSON like object like constants.json file.
- Example:
```
{
    "budget": 10000000,
    "cost": {
        "administrative": 1000000,
        "road": 1000000,
        "school": 1000000,
        "healthcare": 1000000,
        "haat_shop_csc": 1000000,
        "water_facility": 1000000,
        "electric_facility": 1000000,
        "solar_plant": 1000000,
        "biogas": 1000000,
        "windmill": 1000000,
        "sanitation": 1000000
    }
}
```