import pandas as pd
import numpy as np
import sqlite3

# open the database connection
conn = sqlite3.connect("../databases/market_data.db")

# read the data into a pandas dataframe
sql = 'SELECT * from MarketData'
df = pd.read_sql(sql, conn, index_col='Date')



