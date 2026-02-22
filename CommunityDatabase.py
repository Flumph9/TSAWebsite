from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi import FastAPI

class RestaurantBase(SQLModel):
    name: str
    type: str
    address: str
    hours: str
    reviews: float
    price_per_person: str
    website_link: str | None = None


sqlite_file_name = "communitydatabase.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo = True, connect_args=connect_args)


class Restaurant(RestaurantBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class RestaurantCreate(RestaurantBase):
    class Config:
        extra = "forbid"

class GroceryStoreBase(SQLModel):
    name: str
    type: str
    address: str
    hours: str
    reviews: float
    price_range: str
    website_link: str | None = None

class GroceryStore(GroceryStoreBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class GroceryStoreCreate(GroceryStoreBase):
    class Config:
        extra = "forbid"

def populate_restaurants():
    with Session(engine) as session:
        existing = session.exec(select(Restaurant)).first()
        if existing is not None:
            return  # already populated

    rest_1 = Restaurant(name = "Betos", type= "Mexican", address="688 N Main St", hours="Always open", reviews= 4.1, price_per_person="$10-20", website_link="https://www.betos-springville.com/")
    rest_2 = Restaurant(name = "Don Joaquin Street Tacos", type= "Mexican", address="615 N Main St", hours="M-Th: 8 AM-11 PM, F-Sat: 8 AM - 12 AM, Sun: 9 AM - 10PM", reviews= 4.4, price_per_person="$10-20", website_link="https://www.donjoaquinstreettacos.com/en/MENU/")
    rest_3 = Restaurant(name = "La Casita", type= "Mexican", address="333 N Main St", hours="M-Th: 11 AM - 9 PM, F-Sat: 11 AM - 10 PM, Sun: Closed", reviews= 4.4, price_per_person="$10-20")
    rest_4 = Restaurant(name="Cafe Rio", type="Mexican", address="1129 W 400 S, Springville, UT 84663", hours="Daily 11:00 AM - 11:00 PM", reviews=3.6, price_per_person="$10-20", website_link="https://www.caferio.com/locations/springville")
    rest_5 = Restaurant(name="McDonald's", type="Fast Food", address="1455 N Main St, Springville, UT 84663", hours="Open 24 hours", reviews=3.3, price_per_person="$5-10", website_link="https://www.mcdonalds.com/us/en-us/location/UT/SPRINGVILLE/1455-N-MAIN/22757.html")
    rest_6 = Restaurant(name="McDonald's", type="Fast Food", address="961 W 400 S, Springville, UT 84663", hours="Daily 6:00 AM - 11:00 PM", reviews=3.4, price_per_person="$5-10", website_link="https://www.mcdonalds.com/us/en-us/location/UT/SPRINGVILLE/961-W-400-S/22758.html")
    rest_7 = Restaurant(name="McDonald's", type="Fast Food", address="358 S 2000 W, Springville, UT 84663", hours="Open 24 hours", reviews=2.9, price_per_person="$5-10", website_link="https://www.mcdonalds.com/us/en-us/location/UT/SPRINGVILLE/NWC-I-15--400-SOUTH/36752.html")
    rest_8 = Restaurant(name="Magleby's", type="American", address="198 S Main St, Springville, UT 84663", hours="Mon-Tue 11:00 AM - 8:00 PM, Wed Lunch Buffet 11:00 AM - 2:00 PM, Regular 4:00 PM - 8:00 PM, Thu 11:00 AM - 8:00 PM, Fri-Sat 11:00 AM - 9:00 PM, Last Fri of month Buffet 4:00 PM - 9:00 PM, Sun Closed", reviews=4.5, price_per_person="$20-30", website_link="http://www.maglebys.com/")
    rest_9 = Restaurant(name="Pier 49 Pizza", type="Pizza", address="296 S Main St, Springville, UT 84663", hours="Daily 11:00 AM - 9:00 PM", reviews=4.2, price_per_person="$10-20", website_link="http://www.pier49pizzaspringville.com/")
    rest_10 = Restaurant(name="Little Caesars Pizza", type="Pizza", address="405 S Main St, Springville, UT 84663", hours="Daily 11:00 AM - 12:00 AM", reviews=3.3, price_per_person="$5-10", website_link="https://littlecaesars.com/en-us/store/7332")
    rest_11 = Restaurant(name="Strap Tank Brewery", type="American", address="596 S 1750 W, Springville, UT 84663", hours="Daily 11:30 AM - 9:00 PM", reviews=4.2, price_per_person="$10-20", website_link="https://www.straptankbrewery.com/")
    rest_12 = Restaurant(name="T-Bone Chinese American Restaurant", type="Chinese", address="1695 S State St, Springville, UT 84663", hours="Daily 11:00 AM - 9:30 PM", reviews=4.2, price_per_person="$10-20", website_link="https://facebook.com/T-Bone-Restaurant-191550870901501/")
    rest_13 = Restaurant(name="Sidecar Cafe", type="Breakfast", address="1715 W 500 S, Springville, UT 84663", hours="Daily 8:00 AM - 2:00 PM", reviews=4.4, price_per_person="$10-20", website_link="https://thesidecarcafe.com/")
    rest_14 = Restaurant(name="Two Jack's Pizza", type="Pizza", address="171 N Main St, Springville, UT 84663", hours="Daily 11:00 AM - 10:00 PM", reviews=4.5, price_per_person="$10-20", website_link="http://www.twojackspizza.com/")
    rest_15 = Restaurant(name="Subway", type="Sandwiches", address="1055 N Main St, Springville, UT 84663", hours="Daily 8:00 AM - 10:00 PM", reviews=3.3, price_per_person="$5-10", website_link="https://restaurants.subway.com/united-states/ut/springville/1055-n-main-st")
    rest_16 = Restaurant(name="Subway", type="Sandwiches", address="660 S 1750 W, Springville, UT 84663", hours="Daily 8:00 AM - 9:00 PM", reviews=3.3, price_per_person="$5-10", website_link="https://restaurants.subway.com/united-states/ut/springville/660-s-1750-w")

    with Session(engine) as session:
        session.add(rest_1)
        session.add(rest_2)
        session.add(rest_3)
        session.add(rest_4)
        session.add(rest_5)
        session.add(rest_6)
        session.add(rest_7)
        session.add(rest_8)
        session.add(rest_9)
        session.add(rest_10)
        session.add(rest_11)
        session.add(rest_12)
        session.add(rest_13)
        session.add(rest_14)
        session.add(rest_15)
        session.add(rest_16)
        session.commit()

def populate_grocery_stores():
    with Session(engine) as session:
        existing = session.exec(select(GroceryStore)).first()
        if existing is not None:
            return  # already populated

    groc_1 = GroceryStore(name="Whole Foods Market", type="Organic Grocery", address="456 Elm St", hours="8 AM - 10 PM", reviews=4.2, price_range="$$$", website_link="https://www.wholefoodsmarket.com/")
    groc_2 = GroceryStore(name="Trader Joe's", type="Grocery Store", address="789 Oak St", hours="9 AM - 9 PM", reviews=4.5, price_range="$$", website_link="https://www.traderjoes.com/")
    groc_3 = GroceryStore(name="Costco", type="Warehouse Club", address="101 Pine St", hours="10 AM - 8:30 PM", reviews=4.3, price_range="$$", website_link="https://www.costco.com/")

    with Session(engine) as session:
        session.add(groc_1)
        session.add(groc_2)
        session.add(groc_3)
        session.commit()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    populate_restaurants()
    populate_grocery_stores()

@app.post("/restaurants/", response_model=Restaurant)
def create_restaurant(restaurant: RestaurantCreate):
    db_restaurant = Restaurant(**restaurant.dict())
    with Session(engine) as session:
        session.add(db_restaurant)
        session.commit()
        session.refresh(db_restaurant)
        return db_restaurant
    
@app.get("/restaurants/")
def read_restaurants():
    with Session(engine) as session:
        restaurants = session.exec(select(Restaurant)).all()
        return restaurants 

@app.get("/restaurants/{restaurant_id}")
async def read_restaurant(restaurant_id: int):
    with Session(engine) as session:
        restaurant = session.get(Restaurant, restaurant_id)
        if restaurant is None:
            return {"error": "Restaurant not found"}
        return restaurant

@app.get("/restaurants/search/name/")
def search_restaurants_by_name(name: str):
    with Session(engine) as session:
        restaurants = session.exec(select(Restaurant).where(Restaurant.name.contains(name))).all()
        return restaurants

@app.get("/restaurants/search/type/")
def search_restaurants_by_type(type: str):
    with Session(engine) as session:
        restaurants = session.exec(select(Restaurant).where(Restaurant.type == type)).all()
        return restaurants

@app.post("/grocery_stores/", response_model=GroceryStore)
def create_grocery_store_endpoint(grocery_store: GroceryStoreCreate):
    db_grocery_store = GroceryStore(**grocery_store.dict())
    with Session(engine) as session:
        session.add(db_grocery_store)
        session.commit()
        session.refresh(db_grocery_store)
        return db_grocery_store

@app.get("/grocery_stores/")
def read_grocery_stores():
    with Session(engine) as session:
        grocery_stores = session.exec(select(GroceryStore)).all()
        return grocery_stores

@app.get("/grocery_stores/{grocery_store_id}")
async def read_grocery_store(grocery_store_id: int):
    with Session(engine) as session:
        grocery_store = session.get(GroceryStore, grocery_store_id)
        if grocery_store is None:
            return {"error": "Grocery Store not found"}
        return grocery_store
        


        
