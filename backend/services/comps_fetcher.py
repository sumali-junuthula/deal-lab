import pandas as pd

def get_comps():
  df = pd.read_csv("data/sample_comp_deals.csv")
  return df.to_dict(orient="records")
