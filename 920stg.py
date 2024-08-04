import yfinance as yf
from datetime import datetime
import sys

data = yf.download(tickers="^NSEI",start="2023-03-25",end="2023-04-03",interval="1d")

# print(data.iloc[0])

def big_gapup_check(x):
    if(data["Open"].iloc[x+1]-data["Close"].iloc[x]>300):
        return False
    else: 
        return True
    
def tcheck(ltp,i):
    if(high[i]<ltp):
        return 1
    elif(low[i]>ltp):
        return 2
    else:
        return 0
    
ltp=sys.argv[1]
    

for x in range (0,len(data)-1):    
    if (big_gapup_check(x)==True):
        gold = yf.download(tickers="^NSEI", start="2023-03-26",end="2023-04-03", interval="5m")

        y=1
        high=[]
        low=[]

        while y<len(gold):
            high.append(gold["High"].iloc[y])
            low.append(gold["Low"].iloc[y])
            y+=75
        

    new=[]
            
    for i in range(0,len(high)):
        new.append(tcheck(ltp,i))
        i+=1
        