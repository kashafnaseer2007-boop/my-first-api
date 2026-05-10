from fastapi import FastAPI
from pydantic import BaseModel

# Create the robot waiter (the app)
app = FastAPI()

# Homepage: just say hello
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! You're awesome!"}
    from fastapi import FastAPI

# NEW: POST endpoint to receive an order
class Order(BaseModel):
    dish: str
    quantity: int

@app.post("/order")
def create_order(order: Order):
    return {"message": f"Order received: {order.quantity} x {order.dish}"}
