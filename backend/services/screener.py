import yfinance as yf

def get_targets(industry: str, min_market_cap: float):
  tickers = ["AAPL", "MSFT", "TSLA", "GOOG"]  # Replace later with a real list
  results = []

  for ticker in tickers:
    info = yf.Ticker(ticker).info
    if info.get("industry") == industry and info.get("marketCap", 0) >= min_market_cap:
      results.append({
        "ticker": ticker,
        "name": info.get("shortName"),
        "marketCap": info.get("marketCap"),
        "industry": info.get("industry"),
        "revenueGrowth": info.get("revenueGrowth"),
      })
  return results
