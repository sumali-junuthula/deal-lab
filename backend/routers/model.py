from fastapi import APIRouter
from services.accretion import calculate_accretion

router = APIRouter(prefix="/model", tags=["Accretion Model"])

@router.get("/accretion")
def run_model(
  buyer_eps: float,
  target_eps: float,
  synergy: float = 0.0,
  deal_ratio: float = 0.5  # 0.5 means 50% stock, 50% cash
):
  return calculate_accretion(buyer_eps, target_eps, synergy, deal_ratio)
