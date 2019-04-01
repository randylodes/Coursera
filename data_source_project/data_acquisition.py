import quandl
import sqlite3
import numpy as np
import pandas as pd

quandl.ApiConfig.api_key = 'oQc1knDM1rsEN4v4VXc7'
# nas100 = quandl.get('NASDAQOMX/NDX', start_date='2008-05-04', end_date='2018-05-04')
# sp500_month = quandl.get("MULTPL/SP500_REAL_PRICE_MONTH")
data = quandl.get("WIKI/AAPL")

# create the SQLite database connection
conn = sqlite3.connect("../databases/market_data.db")
cur = conn.cursor()

# method to write pandas dataframe directly to SQL db
data.to_sql('MarketData', conn, if_exists='replace')   # if_exists : {‘fail’, ‘replace’, ‘append')





