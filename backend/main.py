from fastapi import FastAPI
from routers import screen  # Add this

app = FastAPI()
app.include_router(screen.router)

@app.get("/")
def root():
  return {"message": "Welcome to DealLab API!"}
