from fastapi import APIRouter
from services.comps_fetcher import get_comps

router = APIRouter(prefix="/comps", tags=["Comps"])

@router.get("/")
def comps():
  return get_comps()
