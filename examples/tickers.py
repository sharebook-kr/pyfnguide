import pyfnguide

tickers = pyfnguide.fetch_tickers()
for comp in tickers:
    print(comp)