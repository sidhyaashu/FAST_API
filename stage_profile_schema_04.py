from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from random import randrange

app = FastAPI()

# Advanced user profile schema
class UserProfile(BaseModel):
    id: Optional[int] = None  # ID will be assigned by the server
    name: str = Field(..., max_length=50, description="Full name of the user")
    email: EmailStr  # Using pydantic's built-in EmailStr validation
    age: Optional[int] = Field(None, ge=18, le=100, description="Age of the user, must be between 18 and 100")
    bio: Optional[str] = Field(None, max_length=300, description="A short bio about the user")
    skills: List[str] = Field([], description="List of skills the user possesses")


# In-memory data store for user profiles (simulates a database)
user_profiles = []

# Retrieve all users
@app.get("/users", response_model=List[UserProfile])
async def get_users():
    return user_profiles

# Retrieve a specific user by ID
@app.get("/users/{user_id}", response_model=UserProfile)
async def get_user(user_id: int):
    user = next((user for user in user_profiles if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create a new user profile
@app.post("/users", response_model=UserProfile)
async def create_user(user: UserProfile = Body(...)):
    user.id = randrange(0, 100000)  # Generate a random ID for the new user
    user_profiles.append(user.dict())
    return user

# Update an existing user profile
@app.put("/users/{user_id}", response_model=UserProfile)
async def update_user(user_id: int, updated_user: UserProfile = Body(...)):
    user = next((user for user in user_profiles if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user profile in place
    user.update(updated_user.dict(exclude_unset=True))
    return user

# Delete a user profile
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    global user_profiles
    user_profiles = [user for user in user_profiles if user["id"] != user_id]
    return {"message": "User deleted successfully"}

# Run the app with: uvicorn filename:app --reload
