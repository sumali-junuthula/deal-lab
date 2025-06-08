import pandas as pd

def get_comps():
  try:
    df = pd.read_csv("data/sample_comp_deals.csv")
    return df.to_dict(orient="records")
  except Exception as e:
    return {"error": str(e)}
