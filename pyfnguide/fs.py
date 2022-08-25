import requests
import datetime
import pandas as pd


def fetch_current_assets(code: str, year: int=None):
    """유동자산

    Args:
        code (str): code used in fnguide (A005930)
        year (int, optional): year
    """
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode={code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=103"
    unit = 100000000

    # 작년 재무제표가 기본값임
    now = datetime.datetime.now()
    last_year = now.year - 1
    if year is None:
        year = last_year

    dfs = pd.read_html(url)
    balance_sheet = dfs[2]
    df = balance_sheet.filter(regex=str(year))
    return int(df.iloc[1, 0] * unit)


def fetch_liabilities(code: str, year: int=None):
    """총부채

    Args:
        code (str): code used in fnguide (A005930)
        year (int, optional): year
    """
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode={code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=103"
    unit = 100000000

    # 작년 재무제표가 기본값임
    now = datetime.datetime.now()
    last_year = now.year - 1
    if year is None:
        year = last_year

    dfs = pd.read_html(url)
    balance_sheet = dfs[2]
    df = balance_sheet.filter(regex=str(year))
    return int(df.iloc[4, 0] * unit)


def fetch_quarterly_net_income(code: str):
    """분기 순이익

    Args:
        code (str): code used in fnguide (A005930)
    """
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode={code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=103"
    unit = 100000000

    now = datetime.datetime.now()
    year = now.year

    dfs = pd.read_html(url)
    income_sheet = dfs[0]
    col0 = income_sheet.columns[0]
    income_sheet.set_index(col0, inplace=True)
    df = income_sheet.filter(regex=str(year))
    return int(df.loc['당기순이익'].iloc[0] * unit)



if __name__ == "__main__":
    #유동자산 = fetch_current_assets("A005930")
    #print(유동자산)

    #부채 = fetch_liabilities("A005930")
    #print(부채)

    #분기순이익 = fetch_quarterly_net_income("A005930")
    #print(분기순이익)