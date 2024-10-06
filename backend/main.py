from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from dash_apps.dash_tool import dash_app  # Import the Dash app
from starlette.middleware.wsgi import WSGIMiddleware  # Import WSGIMiddleware
from sql.sql import get_all_users, add_user  # Import SQL functions

app = FastAPI()

# CORS configuration for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------
# Location Management Endpoints
# ---------------------------------------------

# In-memory "database" with some sample data (both empty and occupied)
locations = [
    {"location_id": "L1", "status": "empty"},
    {"location_id": "L2", "status": "occupied"},
    {"location_id": "L3", "status": "empty"},
    {"location_id": "L4", "status": "occupied"},
    {"location_id": "L5", "status": "empty"},
]

# Pydantic model for locations
class Location(BaseModel):
    location_id: str
    status: str

# Get all empty locations
@app.get("/empty-locations", response_model=List[Location])
def get_empty_locations():
    empty_locations = [location for location in locations if location["status"] == "empty"]
    return empty_locations

# Get all locations (empty and occupied)
@app.get("/all-locations", response_model=List[Location])
def get_all_locations():
    return locations

# Add a new location
@app.post("/empty-locations")
def add_location(location: Location):
    locations.append(location.dict())
    return {"message": "Location added successfully"}

# Delete a location by ID
@app.delete("/empty-locations/{location_id}")
def delete_location(location_id: str):
    global locations
    locations = [location for location in locations if location["location_id"] != location_id]
    return {"message": "Location deleted successfully"}

# Update a location's status
@app.put("/empty-locations/{location_id}")
def update_location(location_id: str, location: Location):
    for loc in locations:
        if loc["location_id"] == location_id:
            loc["status"] = location.status
            return {"message": "Location updated successfully"}
    raise HTTPException(status_code=404, detail="Location not found")

# ---------------------------------------------
# User Management Endpoints (SQL-based)
# ---------------------------------------------

# Pydantic model for the User data
class User(BaseModel):
    name: str
    age: int

# Endpoint to get all users from SQL database
@app.get("/users")
def read_users():
    try:
        users = get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to add a new user to SQL database
@app.post("/users")
def create_user(user: User):
    try:
        add_user(user.name, user.age)
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------------------------
# Dash Tool Integration
# ---------------------------------------------

# Mount the Dash app using WSGIMiddleware
app.mount("/dash-tool", WSGIMiddleware(dash_app.server))
