import uvicorn
from fastapi import FastAPI

from routers import ngram, users

app = FastAPI(title="N-Gram analysis",version="1.0.0")

app.include_router(users.users)
app.include_router(ngram.ngram)


#---------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)