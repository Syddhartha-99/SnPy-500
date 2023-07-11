from time import sleep
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import json
import yfinance as yf
import requests_cache
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

counter = 0

#List of S&P500 constituents
stocks_list = pd.read_csv('sp_500_stocks.csv')
stocks = " "
stocks = stocks.join(stocks_list['Ticker'].tolist())

#Initializes a session to cache scrapped stock information in case of errors
class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

#Session class, from yfinance documentation
session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)

tickers = yf.Tickers(stocks, session = session)


#Building Pandas DataFrame
my_columns = ['Ticker', 'Stock Price', 'Market Capitlization', ' Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)

#Looping through all constituents
for stock in stocks_list['Ticker']:
    print(counter)

    current_ticker = tickers.tickers[str.upper(stock)]

    #Find the market capitalization and price of the selected constituent stock
    try:
        current_price = current_ticker.info['currentPrice']
        market_cap = current_ticker.info['marketCap']
    except KeyError:
        print("Error")

    #Append to Pandas Dataframe
    final_dataframe = final_dataframe._append(pd.Series([str.upper(stock),
                                                        current_price,
                                                        market_cap,
                                                        'N/A'],
                                                        index = my_columns), ignore_index = True)
    counter += 1

print(final_dataframe)