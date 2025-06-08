from fastapi import FastAPI
from routers import screen, comps, model, strategy

app = FastAPI()

app.include_router(screen.router)
app.include_router(comps.router)
app.include_router(model.router)
app.include_router(strategy.router)

@app.get("/")
def root():
  return {"message": "Welcome to DealLab API"}

print("✅ FastAPI is running and routers are registered.")
