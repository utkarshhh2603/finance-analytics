import yfinance as yf

df = yf.download("AAPL MSFT GOOGL", start="2020-01-01", end="2024-12-31")
df.to_csv("data/stocks.csv")
print("Done! stocks.csv saved.")