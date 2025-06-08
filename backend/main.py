from fastapi import FastAPI
from routers import screen, comps  # ✅ Make sure this line exists

app = FastAPI()

app.include_router(screen.router)
app.include_router(comps.router)  # ✅ Register comps here

@app.get("/")
def root():
  return {"message": "Welcome to DealLab API"}

print("✅ FastAPI is running and routers are registered.")
