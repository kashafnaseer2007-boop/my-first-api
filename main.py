from fastapi import FastAPI
from pydantic import BaseModel

# Create the robot waiter (the app)
app = FastAPI()

# Homepage: just say hello
# In-memory DB
greetings_db = {}

@app.get("/hello/{name}")
def say_hello(name: str):
    if name in greetings_db:
        custom = greetings_db[name]
        return {"message": f"{custom}, {name}!"}
    return {"message": f"Hello, {name}! You're awesome!"}

# PUT - update greeting
class GreetingUpdate(BaseModel):
    new_message: str

@app.put("/hello/{name}")
def update_greeting(name: str, update: GreetingUpdate):
    greetings_db[name] = update.new_message
    return {
        "message": f"Greeting for {name} updated!",
        "new_greeting": f"{update.new_message}, {name}!"
    }
    
# POST endpoint to receive an order
favorites_db = []

class FavoriteFood(BaseModel):
    name: str
    food: str

@app.post("/favorite")
def add_favorite(fav: FavoriteFood):
    favorites_db.append(fav)
    return {"message": f"Added {fav.name}'s favorite: {fav.food}"}

# DELETE method to remove a favorite by name
@app.delete("/favorite/{name}")
def delete_favorite(name: str):
    global favorites_db
    # Find and remove the first matching entry
    for i, fav in enumerate(favorites_db):
        if fav.name == name:
            deleted = favorites_db.pop(i)
            return {"message": f"Removed {deleted.name}'s favorite food ({deleted.food})"}
    return {"message": f"No favorite found for {name}"}
