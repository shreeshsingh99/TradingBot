import yfinance as yf
from trailingsl import *
# import sys

data = yf.download(tickers="BTC-USD", start="2023-03-28",end="2023-04-04", interval="1m")
print(data)

x=2
entry_price = 28250
chigh = 28301
clow = 28249

ltp=[]
r=-3

for u in range(0,3):
    ltp.append(float(str(data['Open'].iloc[r])))
    r+=1

print(ltp)

a = initial_SL(entry_price,chigh,clow,x)
b = trailing_SL_1(entry_price,x,ltp[0],a)
print(a)
print(b)

c = trailing_SL_2(a,entry_price,x,ltp[1],b)
print(c)
a,b=c
c = trailing_SL_2(a,entry_price,x,ltp[2],b)
print(c)
