import requests

def fetch_tickers(category='주권'):
    url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
    resp = requests.get(url)
    resp.encoding = "utf-8-sig"
    comp = resp.json()['Co']

    if category == '주권':
        gb = '701'
    elif category == 'ETF':
        gb = '770'
    elif category == 'ETN':
        gb = '780'
    else:
        gb = 'ALL'

    result = [c for c in comp if c['gb'] == gb]
    if gb == 'ALL':
        return comp
    else:
        return result

if __name__ == "__main__":
    tickers = fetch_tickers()
    print(tickers)
