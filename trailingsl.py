def initial_SL(entry_price,chigh,clow,x):
    if (x==1):   #buying
        if(entry_price-clow>=50):
            init_SL = entry_price-50
            return init_SL
        else :
            init_SL = clow
            return init_SL
        
    if (x==2):
        if(chigh-entry_price>=50):
            init_SL = entry_price+50
            return init_SL
        else :
            init_SL = chigh
            return init_SL
        
def trailing_SL_1(entry_price,x,ltp,init_SL):
    if (x==1):               #buy
        if(ltp-entry_price>=entry_price-init_SL):
            trailing_SL=entry_price
            return trailing_SL
        # elif(ltp<=initial_SL):
        #     return "sell"       #loss
        else:
            init_SL = init_SL

    if (x==2):                  #borrow
        if(entry_price-ltp>=init_SL-entry_price):
            trailing_SL = entry_price
            return trailing_SL
        # elif(ltp>=initial_SL):
        #     return "sell"       #loss
        else:
            init_SL = init_SL

def trailing_SL_2(init_SL,entry_price,x,ltp,trailing_SL):
    if(x==1):
        if(ltp-((2*entry_price)-init_SL)>=10):
            trailing_SL = trailing_SL + 5
            init_SL = ltp
            return init_SL,trailing_SL
        elif(ltp>=init_SL + 10):
            trailing_SL = trailing_SL + 5
            init_SL = ltp
            return init_SL, trailing_SL
        else:
            return 0
    if(x==2):
        if(((2*entry_price)-init_SL-ltp)>=10):
            trailing_SL = trailing_SL -5
            init_SL = ltp
            return init_SL,trailing_SL
        elif(init_SL-ltp>=10):
            trailing_SL = trailing_SL -5
            init_SL = ltp
            return init_SL, trailing_SL
        else :
            return 0

        


    
