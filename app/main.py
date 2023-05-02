from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

import uvicorn 


app = FastAPI() 

@app.get("/") 
def home(): 
    return {"message": "Welcome to Axialis"}

if __name__ == '__main__': 
    app.run("main:app", host="0.0.0.0", port=8080, reload=True)