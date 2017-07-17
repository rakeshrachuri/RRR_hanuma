#Feature 1.1
# Read 15 min OHLC candle sticks from alpha vantage
# Prepare standardized panda data frame and return for calling module
import com.rrr.dr.alphaVantageDataReader as avd
import pandas as pd
class DataReader:

    def __init__(self, dataProviderName,symbol):
        self.dataProviderName = dataProviderName
        self.symbol=symbol
        if self.dataProviderName=='alphavantage':
            self.alphaVantage= avd.AlphaVantageDataReaderClass()

    def getIntraDayData(self,ohlcsize):
        if self.dataProviderName=='alphavantage':
            return self.alphaVantage.getIntraDayData(ohlcsize,self.symbol)


#dr=DataReader('alphavantage','AAPL')
#ohlc_dataFrame=dr.getIntraDayData(15)
#print(ohlc_dataFrame['volume'])

