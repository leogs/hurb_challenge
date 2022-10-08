from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {'Status': 'Fine'}

if __name__ == '__main__':
    uvicorn.run('main:app')