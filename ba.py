import talib
import pandas as pd
import numpy as np
from datetime import datetime  
import yfinance as yf 
import sys  
from trailingsl import *                                                                                                    

# Load data
data = yf.download(tickers="^NSEI",start="2023-03-25",end="2023-04-03",interval="1d")

# print(data.iloc[0])

def gapup(x):
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
    if (gapup(x)==True):
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


# Define trading strategy based on technical indicators


# Initialize trading parameters
position = 0  # 0 = no position, 1 = long position, -1 = short position
capital = 1000000  # Initial capital
trade_size = 1000  # Fixed trade size
fees = 0.001  # Transaction fees

# Initialize lists to store trading results
balance = [capital]
equity = [capital]

# Loop through each trading day
for i in range(0, len(new)):
    # Check if there is a trading signal
    if (new[i]==1):
        if position == 0:
            # Enter long position
            position = 1
            entry_price = high[i]
            # trade_cost = entry_price * trade_size * fees
            # balance.append(balance[-1] - trade_cost)
        elif position == -1:
            # Exit short position and enter long position
            position = 1
            exit_price = data['close'][i]
            trade_profit = (entry_price - exit_price) * trade_size
            #print(trade_profit,i)
            trade_cost = (entry_price + exit_price) * trade_size * fees
            balance.append(balance[-1] + trade_profit - trade_cost)
        else:
            # Already in long position, do nothing
            balance.append(balance[-1])
    elif (new[i]==2):
        if position == 0:
            # Enter short position
            position = -1
            entry_price = data['close'][i]
            trade_cost = entry_price * trade_size * fees
            balance.append(balance[-1] - trade_cost)
        elif position == 1:
            # Exit long position and enter short position
            position = -1
            exit_price = data['close'][i]
            trade_profit = (exit_price - entry_price) * trade_size
            print(trade_profit,i)
            trade_cost = (entry_price + exit_price) * trade_size * fees
            balance.append(balance[-1] + trade_profit - trade_cost)
        else:
            # Already in short position, do nothing
            balance.append(balance[-1])
    else:
        # No trading signal, do nothing
        balance.append(balance[-1])

    equity.append(balance[-1] + position * trade_size * data['close'][i])


