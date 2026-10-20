import uvicorn
from fastapi import FastAPI

app = FastAPI(title="N-Gram analysis")

@app.get("/test")
def test ():
    return {"status":"all good"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)