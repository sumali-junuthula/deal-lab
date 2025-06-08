from fastapi import APIRouter
from services.gpt_summary import generate_strategy

router = APIRouter(prefix="/strategy", tags=["Strategy"])

@router.get("/")
def strategy(buyer: str, target: str):
  return generate_strategy(buyer, target)
