import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import json
import yfinance as yf


#List of S&P500 constituents
stocks = pd.read_csv('sp_500_stocks.csv')

#Building Pandas DataFrame
my_columns = ['Ticker', 'Stock Price', 'Market Capitlization', ' Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)

#Looping through all constituents
for stock in stocks['Ticker']:

    #Find the market capitalization and price of the selected company
    current_price = yf.Ticker(stock).info['currentPrice']
    market_cap = yf.Ticker(stock).info['marketCap']

    final_dataframe = final_dataframe._append(pd.Series([stock,
                                                        current_price,
                                                        market_cap,
                                                       'N/A'],
                                                        index = my_columns), ignore_index = True)

print(final_dataframe)



##Testing stuff
#msft = yf.Ticker("MSFT")
#print("Microsoft Current Market Price : ", msft.info['currentPrice'])

#def search_key_by_keyword(data: dict, keyword: str) -> list[str]:
#    return list(filter(lambda x: keyword in x.lower(), data.keys()))

#valid_market_keys = search_key_by_keyword(msft.info, "cap")
#print(valid_market_keys)