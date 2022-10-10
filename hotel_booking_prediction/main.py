from fastapi import FastAPI, Depends
import uvicorn

import auth
from auth import get_current_user
from routers import prediction
from config import settings

PROTECTED = [Depends(get_current_user)]

app = FastAPI()
app.include_router(auth.router)
app.include_router(
    prediction.router,
    dependencies=PROTECTED)

@app.get("/")
def home():
    return {'Status': 'Fine'}

if __name__ == '__main__':
    uvicorn.run('main:app')