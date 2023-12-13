import json

import yfinance as yf
import pandas as pd

from pandas.tseries.offsets import BDay

from gauss_ai.utils import get_config, get_url

CONFIG = get_config("yfinance")


def load_data(symbol, start_date=None, end_date=None, interval='1d'):
    """
    Fetches data from Yahoo Finance for a given stock symbol.

    Args:
        symbol (str): The stock symbol to fetch data for.
        start_date (str): Start date of the data in YYYY-MM-DD format.
        end_date (str): End date of the data in YYYY-MM-DD format.
        interval (str): Data interval (e.g., '1d' for daily).

    Returns:
        pandas.DataFrame: DataFrame containing the fetched stock data.
    """
    # Fetch data using yfinance
    stock = yf.Ticker(symbol)
    yesterday = (pd.Timestamp.today() - BDay(1)).strftime("%Y-%m-%d")
    prev_date = (pd.Timestamp.today() - BDay(20)).strftime("%Y-%m-%d")
    start_date = prev_date if start_date is None else pd.to_datetime(start_date).strftime("%Y-%m-%d")
    end_date = yesterday if end_date is None else pd.to_datetime(end_date).strftime("%Y-%m-%d")
    data = stock.history(start=start_date, end=end_date, interval=interval)

    return data


def request_headers():
    headers = {
        'authority': 'query1.finance.yahoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
        'cache-control': 'max-age=0',
        'cookie': 'GUC=AQEBCAFkeFlkokIfUwSP&s=AQAAAKu91_s4&g=ZHcWPw; '
                  'A1=d=AQABBBrgWWQCEOwcAsk_Csckn73PvZULxXgFEgEBCAFZeGSiZFlQb2UB_eMBAAcIGuBZZJULxXg&S'
                  '=AQAAApxmDx1U3f9yRT_gshYcnoY; '
                  'A3=d=AQABBBrgWWQCEOwcAsk_Csckn73PvZULxXgFEgEBCAFZeGSiZFlQb2UB_eMBAAcIGuBZZJULxXg&S'
                  '=AQAAApxmDx1U3f9yRT_gshYcnoY; cmp=t=1685526084&j=0&u=1---; '
                  'PRF=t%3DGOLDBEES.NS%252BNIFTY_FIN_SERVICE.NS%26newChartbetateaser%3D1; '
                  'A1S=d=AQABBBrgWWQCEOwcAsk_Csckn73PvZULxXgFEgEBCAFZeGSiZFlQb2UB_eMBAAcIGuBZZJULxXg&S'
                  '=AQAAApxmDx1U3f9yRT_gshYcnoY',
        'sec-ch-ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                      'Safari/537.36', }
    return headers


def query_name(name: str):
    base_url = CONFIG['QUERY_URL']['BASE_URL']
    query = CONFIG['QUERY_URL']['QUERY']
    my_query = query.replace("NIFTY", name.upper())
    response = get_url(url=f"{base_url}?{my_query}", headers=request_headers())
    json_obj = json.loads(response)
    return json_obj['quotes']


def check_symbol(symbol: str) -> bool:
    if symbol is not None:
        ticker = yf.Ticker(symbol)
        return ticker.history().shape[0] > 0


# Example usage
if __name__ == "__main__":
    # Example for fetching AAPL data
    aapl_data = load_data('AAPL', '2020-01-01', '2021-01-01')
    print(aapl_data.head())
