from fastapi import APIRouter

ngram = APIRouter()

@ngram.get("/begram", tags=["N-Gram"])
def begram():
    return {"status":"all good"}

@ngram.get("/threegram", tags=["N-Gram"])
def threegram():
    return {"status":"all good"}

@ngram.get("/fourgram", tags=["N-Gram"])
def fourgram():
    return {"status":"all good"}