from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from osm_client import get_places_by_tag, get_place_details

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

TAGS = {
    "amenity": [
        "school", "college", "library",
        "hospital", "clinic", "doctors", "dentist", "pharmacy",
        "fire_station", "police",
        "restaurant", "cafe", "fast_food", "bar", "ice_cream",
        "bank", "atm", "fuel", "car_wash", "car_repair",
        "park", "playground", "gym", "sports_centre",
        "community_centre", "place_of_worship",
        "post_office", "townhall"
    ],
    "shop": [
        "supermarket", "convenience", "clothes", "electronics",
        "hardware", "bakery", "butcher", "pharmacy", "florist"
    ],
    "leisure": [
        "park", "playground", "sports_centre",
        "fitness_centre", "golf_course"
    ],
    "tourism": [
        "hotel", "motel", "museum",
        "attraction", "viewpoint"
    ]
}


@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.get("/tags")
def available_tags():
    return TAGS


@app.get("/places/{tag_type}/{tag_value}")
def places(tag_type: str, tag_value: str):
    if tag_type not in TAGS or tag_value not in TAGS[tag_type]:
        return JSONResponse({"error": "Unsupported tag"}, status_code=400)

    return get_places_by_tag(tag_type, tag_value)


@app.get("/place/{place_id}", response_class=HTMLResponse)
def place(place_id: int):
    return get_place_details(place_id)