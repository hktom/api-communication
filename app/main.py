from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

import uvicorn 

from routes.communications import communications_router


app = FastAPI() 

# register route 
app.include_router(communications_router) 

@app.on_event("startup") 
def on_startup(): 
    # Initialize the database here.
    pass

@app.get("/") 
def home(): 
    return {"message": "Welcome to Axialis"}

if __name__ == '__main__': 
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)