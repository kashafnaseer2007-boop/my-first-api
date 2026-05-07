# --------------- GET METHOD ---------------

    # from fastapi import FastAPI

    # app = FastAPI()


    # items = {
    #     1: {"name": "Laptop", "price": 1000},
    #     2: {"name": "Phone", "price": 500}
    # }

    # @app.get("/items/{item_id}")
    # def get_item(item_id: int):
    #     return items.get(item_id, {"error": "Item not found"})

# --------------- POST METHOD ---------------

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# items = {}

# # Data model
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = False

# # CREATE (POST)
# @app.post("/items/{item_id}")
# def create_item(item_id: int, item: Item):
#     items[item_id] = item
#     return {"message": "Item created", "item": item}

from fastapi import HTTPException

# -------------- PUT METHOD ---------------

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    
    items[item_id] = item
    return {"message": "Item fully updated", "item": item}


# -------------- DELETE METHOD ---------------

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}