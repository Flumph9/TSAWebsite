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
    address: str
    hours: str
    website_link: str | None = None

class GroceryStore(GroceryStoreBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class GroceryStoreCreate(GroceryStoreBase):
    class Config:
        extra = "forbid"

class GasStationBase(SQLModel):
    name: str
    address: str
    hours: str
    website_link: str | None = None

class GasStation(GasStationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class GasStationCreate(GasStationBase):
    class Config:
        extra = "forbid"

class CommunityServiceBase(SQLModel):
    name: str
    type: str
    address: str
    hours: str
    phone: str | None = None
    website_link: str | None = None

class CommunityService(CommunityServiceBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class CommunityServiceCreate(CommunityServiceBase):
    class Config:
        extra = "forbid"

class SchoolBase(SQLModel):
    name: str
    type: str
    address: str
    hours: str
    phone: str | None = None
    website_link: str | None = None

class School(SchoolBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class SchoolCreate(SchoolBase):
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
        
    groc_1 = GroceryStore(name="Smith's", address="1117 W 400 S, Springville, UT 84663", hours="Open 24 Hours", website_link="https://www.smithsfoodanddrug.com/")
    groc_2 = GroceryStore(name="Walmart", address="660 S 1750 W, Springville, UT 84663", hours="Daily 6 AM - 11 PM", website_link="https://www.walmart.com/")
    groc_3 = GroceryStore(name="Ream's", address="759 E 400 S, Springville, UT 84663", hours="Daily 6 AM - 10 PM", website_link="https://shop.springvillereams.com/")
    groc_4 = GroceryStore(name="Redmond Heritage Farm Store", address="445 N 2000 W Unit 5, Springville, UT 84663", hours="Daily 10 AM - 6 PM", website_link="https://www.redmondfarms.com/")

    with Session(engine) as session:
        session.add(groc_1)
        session.add(groc_2)
        session.add(groc_3)
        session.add(groc_4)
        session.commit()

def populate_gas_stations():
    with Session(engine) as session:
        existing = session.exec(select(GasStation)).first()
        if existing is not None:
            return  # already populated
    
    gas_1 = GasStation(name="Maverik", address="309 N Main St, Springville, UT 84663", hours="Open 24 Hours", website_link="https://locations.maverik.com/ut/springville/309-n-main-st")
    gas_2 = GasStation(name="Shell", address="171 N Main St, Springville, UT 84663", hours="Open 24 Hours", website_link="https://find.shell.com/us/fuel/12836397-171-n-main-st/en_US")
    gas_3 = GasStation(name="Maverik", address="1509 N 1750 W, Springville, UT 84663", hours="Open 24 Hours", website_link="https://locations.maverik.com/ut/springville/1509-no-1750-w")
    gas_4 = GasStation(name="Chevron", address="395 S Main St, Springville, UT 84663", hours="Daily 6 AM - 10 PM", website_link="https://www.chevron.com/")
    gas_5 = GasStation(name="Love's Travel Stop", address="358 S 2200 W, Springville, UT 84663", hours="Open 24 Hours", website_link="https://www.loves.com/")
    gas_6 = GasStation(name="Pilot Travel Center", address="1460 N 1750 W, Springville, UT 84663", hours="Open 24 Hours", website_link="https://locations.pilotflyingj.com/")
    gas_7 = GasStation(name="7-Eleven", address="1400 N Main St, Springville, UT 84663", hours="Open 24 Hours", website_link="https://www.7-eleven.com/")
    gas_8 = GasStation(name="Jake's Brookside", address="410 S 400 E, Springville, UT 84663", hours="Daily 10 AM - 11 PM", website_link="https://www.jakesbrookside.com/")

    with Session(engine) as session:
        session.add(gas_1)
        session.add(gas_2)
        session.add(gas_3)
        session.add(gas_4)
        session.add(gas_5)
        session.add(gas_6)
        session.add(gas_7)
        session.add(gas_8)
        session.commit()

def populate_community_services():
    with Session(engine) as session:
        existing = session.exec(select(CommunityService)).first()
        if existing is not None:
            return  # already populated
    
    service_1 = CommunityService(name="Springville Public Library", type="Library", address="45 S Main St, Springville, UT 84663", hours="Mon-Thu 10 AM - 9 PM, Fri 10 AM - 6 PM, Sat 10 AM - 5 PM, Sun Closed", phone="(801) 489-2720", website_link="https://www.springvilleutah.gov/library/")
    service_2 = CommunityService(name="Springville Police Department", type="Police", address="110 S Main St, Springville, UT 84663", hours="Open 24 Hours", phone="(801) 489-9421", website_link="https://www.springville.org/police/")
    service_3 = CommunityService(name="Springville Fire Dept. Station 42", type="Fire Station", address="420 Canyon Rd, Springville, UT 84663", hours="24/7", phone="(801) 491-5600", website_link="https://www.springville.org/fire-rescue/about/")
    service_4 = CommunityService(name="Springville Fire and Rescue Station 41", type="Fire Station", address="75 W Center St, Springville, UT 84663", hours="24/7", phone="(801) 489-9421", website_link="https://www.springville.org/fire-rescue/about/")
    service_5 = CommunityService(name="Springville City Recreation Department", type="Recreation Center", address="443 S 200 E #2229, Springville, UT 84663", hours="Daily 9 AM - 10 PM", phone="(801) 489-2770", website_link="https://www.springville.org/parks-recreation/recreation/")
    service_6 = CommunityService(name="Springville Senior Citizens Center", type="Senior Center", address="65 E 200 S, Springville, UT 84663", hours="Mon-Fri 10 AM - 4 PM, Sat-Sun Closed", phone="(801) 489-8738", website_link="http://www.springvilleseniorcenter.org/")
    service_7 = CommunityService(name="Springville Utah FamilySearch Center", type="Research Center", address="260 S 700 E, Springville, UT 84663", hours="Mon-Thu 7 PM - 9 PM, Fri 10 AM - 2 PM, Sat 10 AM - 2 PM, Sun Closed", phone="(801) 489-2956", website_link="https://www.familysearch.org/en/centers/springville_utah/")
    service_8 = CommunityService(name="Springville Civic Center", type="City Hall", address="110 S Main St, Springville, UT 84663", hours="Mon-Fri 8 AM - 5 PM, Sat-Sun Closed", phone="(801) 489-2700", website_link="https://www.springvilleutah.gov/")

    with Session(engine) as session:
        session.add(service_1)
        session.add(service_2)
        session.add(service_3)
        session.add(service_4)
        session.add(service_5)
        session.add(service_6)
        session.add(service_7)
        session.add(service_8)
        session.commit()

def populate_schools():
    with Session(engine) as session:
        existing = session.exec(select(School)).first()
        if existing is not None:
            return  # already populated
    
    school_1 = School(name="Springville High School", type="High School", address="1205 E 900 S, Springville, UT 84663", hours="Mon-Fri 7:55 AM - 3:30 PM", phone="(801) 489-2870", website_link="http://shs.nebo.edu/")
    school_2 = School(name="Merit Preparatory Academy", type="Charter School", address="1440 W Center St, Springville, UT 84663", hours="Mon-Fri 8:30 AM - 3:30 PM", phone="(801) 491-7600", website_link="http://meritprepacademy.org/")
    school_3 = School(name="Reagan Academy", type="Middle School", address="1143 W Center St, Springville, UT 84663", hours="Mon-Fri 8:00 AM - 3:30 PM", phone="(801) 489-7828", website_link="https://www.reaganacademy.org/")
    school_4 = School(name="Art City Elementary School", type="Elementary School", address="121 N 900 E, Springville, UT 84663", hours="Mon-Fri 8:00 AM - 3:30 PM", phone="(801) 489-2820", website_link="http://artcity.nebo.edu/")
    school_5 = School(name="Cherry Creek Elementary School", type="Elementary School", address="484 S 200 E, Springville, UT 84663", hours="Mon-Fri 8:30 AM - 3:30 PM", phone="(801) 489-2810", website_link="http://cherrycreek.nebo.edu/")
    school_6 = School(name="Westside Elementary School", type="Elementary School", address="740 W Center St, Springville, UT 84663", hours="Mon-Fri 8:00 AM - 3:30 PM", phone="(801) 489-2800", website_link="http://westside.nebo.edu/")

    with Session(engine) as session:
        session.add(school_1)
        session.add(school_2)
        session.add(school_3)
        session.add(school_4)
        session.add(school_5)
        session.add(school_6)
        session.commit()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    populate_restaurants()
    populate_grocery_stores()
    populate_gas_stations()
    populate_community_services()
    populate_schools()

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

@app.post("/gas_stations/", response_model=GasStation)
def create_gas_station_endpoint(gas_station: GasStationCreate):
    db_gas_station = GasStation(**gas_station.dict())
    with Session(engine) as session:
        session.add(db_gas_station)
        session.commit()
        session.refresh(db_gas_station)
        return db_gas_station

@app.get("/gas_stations/")
def read_gas_stations():
    with Session(engine) as session:
        gas_stations = session.exec(select(GasStation)).all()
        return gas_stations

@app.get("/gas_stations/{gas_station_id}")
async def read_gas_station(gas_station_id: int):
    with Session(engine) as session:
        gas_station = session.get(GasStation, gas_station_id)
        if gas_station is None:
            return {"error": "Gas Station not found"}
        return gas_station

@app.post("/community_services/", response_model=CommunityService)
def create_community_service_endpoint(community_service: CommunityServiceCreate):
    db_community_service = CommunityService(**community_service.dict())
    with Session(engine) as session:
        session.add(db_community_service)
        session.commit()
        session.refresh(db_community_service)
        return db_community_service

@app.get("/community_services/")
def read_community_services():
    with Session(engine) as session:
        community_services = session.exec(select(CommunityService)).all()
        return community_services

@app.get("/community_services/{community_service_id}")
async def read_community_service(community_service_id: int):
    with Session(engine) as session:
        community_service = session.get(CommunityService, community_service_id)
        if community_service is None:
            return {"error": "Community Service not found"}
        return community_service

@app.post("/schools/", response_model=School)
def create_school_endpoint(school: SchoolCreate):
    db_school = School(**school.dict())
    with Session(engine) as session:
        session.add(db_school)
        session.commit()
        session.refresh(db_school)
        return db_school

@app.get("/schools/")
def read_schools():
    with Session(engine) as session:
        schools = session.exec(select(School)).all()
        return schools

@app.get("/schools/{school_id}")
async def read_school(school_id: int):
    with Session(engine) as session:
        school = session.get(School, school_id)
        if school is None:
            return {"error": "School not found"}
        return school

