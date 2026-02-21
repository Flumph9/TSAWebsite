import requests


CACHE = {}

def cached_overpass_query(cache_key: str, query: str):
    if cache_key in CACHE:
        return CACHE[cache_key]

    data = overpass_query(query)

    if (
        not isinstance(data, dict)
        or "elements" not in data
        or not data["elements"]
    ):
        return data

    CACHE[cache_key] = data
    return data

OVERPASS_URL = "https://overpass-api.de/api/interpreter"




def overpass_query(query: str):
    response = requests.post(
        OVERPASS_URL,
        data=query,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30
    )

    try:
        return response.json()
    except ValueError:
        return {
            "error": "Invalid response from Overpass",
            "raw_response": response.text[:300]
        }


def get_places_by_tag(tag_type: str, tag_value: str):
    cache_key = f"{tag_type}:{tag_value}"

    query = f"""
    [out:json][timeout:25];

    area["name"="Utah"]["boundary"="administrative"]["admin_level"="4"]->.utah;
    area["name"="Springville"]["boundary"="administrative"]["admin_level"="8"](area.utah)->.springville;

    (
      node["{tag_type}"="{tag_value}"](area.springville);
      way["{tag_type}"="{tag_value}"](area.springville);
    );

    out tags 50;
    """

    return cached_overpass_query(cache_key, query)


def get_place_details(place_id: int):
    query = f"""
    [out:json];
    (
      node({place_id});
      way({place_id});
      relation({place_id});
    );
    out center tags;
    """

    data = overpass_query(query)

    if not data.get("elements"):
        return "<pre>Place not found</pre>"

    el = data["elements"][0]
    lines = []

    lines.append(f"id: {el.get('id')}")
    lines.append(f"type: {el.get('type')}")

    if "lat" in el and "lon" in el:
        lines.append(f"lat: {el['lat']}")
        lines.append(f"lon: {el['lon']}")
    elif "center" in el:
        lines.append(f"lat: {el['center'].get('lat')}")
        lines.append(f"lon: {el['center'].get('lon')}")

    tags = el.get("tags", {})

    if tags:
        lines.append("\n--- tags ---")
        for k, v in tags.items():
            lines.append(f"{k}: {v}")
    else:
        lines.append("\n(no tags available for this place)")

    return "<pre>" + "\n".join(lines) + "</pre>"

    data = overpass_query(query)

    if not data.get("elements"):
        return "<pre>Place not found</pre>"

    tags = data["elements"][0].get("tags", {})
    text = "\n".join(f"{k}: {v}" for k, v in tags.items())
    return f"<pre>{text}</pre>"