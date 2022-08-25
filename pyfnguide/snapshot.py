import requests
from bs4 import BeautifulSoup


def fetch_market_cap(code: str) -> int:
    """시가총액 (보통주)

    Args:
        code (str): fnguide code

    Returns:
        int: 시가총액
    """
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode={code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=101"
    unit = 100000000
    resp = requests.get(url)
    html = resp.text

    selector = "#svdMainGrid1 > table > tbody > tr:nth-child(5) > td:nth-child(2)"
    soup = BeautifulSoup(html, features="html5lib")
    tags = soup.select(selector)[0]
    text = tags.text
    market_cap = int(text.replace(',', '')) * unit
    return market_cap


if __name__ == "__main__":
    시가총액 = fetch_market_cap("A005930")
    print(시가총액)
