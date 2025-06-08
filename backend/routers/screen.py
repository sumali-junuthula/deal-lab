from fastapi import APIRouter, Query
from services.screener import get_targets

router = APIRouter(prefix="/screen", tags=["Screener"])

@router.get("/targets")
def screen_targets(industry: str = "Technology", min_market_cap: float = 1e9):
  return get_targets(industry, min_market_cap)
