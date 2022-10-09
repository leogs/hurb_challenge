from fastapi import FastAPI
import uvicorn

from hotel_booking_prediction.routers import prediction

app = FastAPI()

app.include_router(prediction.router)

@app.get("/")
def home():
    return {'Status': 'Fine'}

if __name__ == '__main__':
    uvicorn.run('main:app')