import yfinance as yf

def get_targets(industry: str, min_market_cap: float):
  tickers = ["AAPL", "MSFT", "TSLA", "GOOG", "AMZN", "NVDA", "INTC", "CRM"]
  results = []

  for ticker in tickers:
    try:
      info = yf.Ticker(ticker).info

      if info.get("marketCap", 0) >= min_market_cap:
        results.append({
          "ticker": ticker,
          "name": info.get("shortName"),
          "industry": info.get("industry"),
          "marketCap": info.get("marketCap"),
          "revenueGrowth": info.get("revenueGrowth"),
          "ebitdaMargins": info.get("ebitdaMargins"),
          "forwardPE": info.get("forwardPE"),
          "recommendation": info.get("recommendationKey"),
          "targetPrice": info.get("targetMeanPrice")
        })
    except Exception:
      continue

  return sorted(results, key=lambda x: x['marketCap'], reverse=True)

