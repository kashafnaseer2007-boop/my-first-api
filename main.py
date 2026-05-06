from fastapi import FastAPI

# Create the robot waiter (the app)
app = FastAPI()

# Homepage: just say hello
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! You're awesome!"}