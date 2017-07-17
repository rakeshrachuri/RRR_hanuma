import com.rrr.dr.dataReader as dr_pkg

#import com.rrr.renderer.screenManager as sm_pkg


dr=dr_pkg.DataReader('alphavantage','AAPL')
ohlc_dataFrame=dr.getIntraDayData(15)
#sm=sm_pkg.ScreenManager()
#sm.updateView(ohlc_dataFrame)