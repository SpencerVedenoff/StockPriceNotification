import pandas as pd
import time
import smtplib

# Gets data
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='7CMNQJZTBJHKBFJZ', output_format='pandas')

data, meta_data = ts.get_intraday(symbol='NVDA',interval='60min', outputsize='full')

close_data = data['4. close']
last_price = close_data[0]

print(last_price)
