from fastapi import FastAPI

app = FastAPI(
  title="DealLab API",
  description="AI-powered M&A analysis toolkit",
  version="1.0.0"
)

@app.get("/")
def root():
  return {"message": "Welcome to DealLab API!"}
