# pyfnguide
python wrapper of the fnguide for the quantitative trading

## 종목 정보

```
import pyfnguide
tickers = pyfnguide.fetch_tickers()
```

## 팩터

```
import pyfnguide
유동자산 = pyfnguide.fetch_current_assets("A005930")
```


| 지표 | 함수 | 사용되는 전략 |
|-----|-----|-----|
| 유동자산 | `fetch_current_assets("A005930")` | NCAV |
| 총부채 | `fetch_liabilities("A005930")` | NCAV |
| 시가총액 | `fetch_maket_cap("A005930")` | NCAV |
| 분기 순이익 | `fetch_quarterly_net_income("A00593")` | NCAV |
