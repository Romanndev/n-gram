from fastapi import APIRouter

users = APIRouter()

@users.get("/users",tags=["Users"])
def registration():
    return {"status":"all good"}

