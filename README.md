# Robot Waiter API – First FastAPI Practice

A simple, fun **Robot Waiter** API that greets you by your name.  
Built with **FastAPI** – my first API project to practice REST endpoints and path parameters.

## Features

- One friendly endpoint: `GET /hello/{name}`
- Returns a personalized JSON greeting
- Auto-documented Swagger UI at `/docs`

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation & Running

1. Save the Python code below as `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! You're awesome!"}
