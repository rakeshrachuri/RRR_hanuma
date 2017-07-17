#Alphavantage data reader
import urllib3
#from urllib3 import request
import json
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import exceptions


class AlphaVantageDataReaderClass:
    def __init__(self,trace=False):
        self.trace=trace
        self.urlToVisit='https://www.alphavantage.co/query?'
        self.apiKey='QMADQJAXN0QR6DNU'
        self.http=urllib3.PoolManager()


    def getIntraDayData(self,ohlcSize,symbol):
        urllib3.disable_warnings(exceptions.InsecureRequestWarning)

        urlToVisit=self.urlToVisit+ \
                       'function=TIME_SERIES_INTRADAY&symbol={0}&interval={1}min&apikey={2}'\
                       .format(symbol,ohlcSize,self.apiKey)
        if self.trace == True:
            print('URL being hit:'+urlToVisit)
        r=self.http.request('GET',urlToVisit)

        #jsob.loads converts raw data into data dictionary with key value pairs
        stockData=json.loads(r.data.decode('utf-8'))
        if self.trace == True:
            print('Data loaded from URL')
            print(stockData)
        #ignore meta data and pass only time series information

        return self.wrangleData(stockData['Time Series ('+str(ohlcSize)+'min)'])

    def wrangleData(self,stockData):
        """

        :rtype: pandas.DataFrame
        """
        if self.trace == True:
            print('Inside wrangle Data method')
        #Prepare data frame based on dictionary stock data
        assert isinstance(stockData, dict)
        stock_df = pd.DataFrame(stockData)
        # Transposing data means, making rows to columns and vice versa, open, high,low,close,
        # volume will be columns now
        stock_df=stock_df.T
        #renaming columns properly, removing unnecessary spaces and numbers
        stock_df.rename(columns=lambda x: x[3:], inplace=True)
        #stock_df.columns.tolist()
        return stock_df






#test=AlphaVantageDataReaderClass(trace=True)
#test.getIntraDayData(15,'AAPL')
#print(test.getIntraDayData(15,'AAPL'))

