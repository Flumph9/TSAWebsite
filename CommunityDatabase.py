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


sqlite_file_name = "restaurants.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo = True, connect_args=connect_args)


class Restaurant(RestaurantBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class RestaurantCreate(RestaurantBase):
    class Config:
        extra = "forbid"

def create_restaurant():
    rest_1 = Restaurant(name = "Betos", type= "Mexican", address="688 N Main St", hours="Always open", reviews= 4.1, price_per_person="$10-20", website_link="https://www.betos-springville.com/")
    rest_2 = Restaurant(name = "Don Joaquin Street Tacos", type= "Mexican", address="615 N Main St", hours="M-Th: 8 AM-11 PM, F-Sat: 8 AM - 12 AM, Sun: 9 AM - 10PM", reviews= 4.4, price_per_person="$10-20", website_link="https://www.donjoaquinstreettacos.com/en/MENU/")
    rest_3 = Restaurant(name = "La Casita", type= "Mexican", address="333 N Main St", hours="M-Th: 11 AM - 9 PM, F-Sat: 11 AM - 10 PM, Sun: Closed", reviews= 4.4, price_per_person="$10-20")

    with Session(engine) as session:
        session.add(rest_1)
        session.add(rest_2)
        session.add(rest_3)
        session.commit()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

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


        