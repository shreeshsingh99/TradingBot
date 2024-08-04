from tvDatafeed import TvDatafeed, Interval
tv = TvDatafeed()

nifty_index_data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_1_minute,n_bars=10)

print(nifty_index_data)

#Defining Candles
def Candle_color(df):
    open = df.open.iloc[-1]
    close = df.close.iloc[-1]

    #red
    if(open>close):
        return 1
    #green
    if(open<close):
        return 2

# val = Candle_color(nifty_index_data)
# print(val)




    
