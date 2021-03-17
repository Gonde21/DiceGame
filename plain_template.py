import numpy as np
from timeit import default_timer as timer
from decimal import Decimal

def dobet():
    #Main Variables
    base = 2
    chance = 50
    capital = 500
    basecapital = capital
    M = 100
    multiplier = 9900/(10000*chance)
    multi = int(multiplier)
    print(multi)

    #Ignore
    dic = chance*100
    previousbet = base
    nextbet = base
     

    #Bolean Win Loss
    win = 0
    lastgame = 0
    
    #Stats
    biggestbet = 0
    count = 0
    countm = 0
    death = 0
    wagered = 0

    start = timer()
    #Dataset
    million = 1
    size = million*1000000

    #Create 10 smaller datasets and go through them one by one
    for numbers in range(10):

        #Random Number generator. Ints from 1-9999
        rng = np.random.default_rng()
        test_data = rng.integers(1, high=10000, size=size)

        #Apply or strategy and see how it performs
        for x in test_data:
            #Win and loss definition
            if x<dic:
                win = 1 
            else:
                win = 0
            count += 1

            if win==1: 
                capital += previousbet*multi
                lastgame = 1
            else:
                capital = (capital+capital) - previousbet*100000
                lastgame = 0

            #Strategy
            if win:
                nextbet=base
            else:
                nextbet = previousbet
            
            #Late Calculations
            if nextbet>biggestbet:
                biggestbet=nextbet
            
            if capital<0:
                death +=1
                nextbet=base
                capital = basecapital

            #Print this each 1M games   
            if count % 1000000 == 0:
                countm +=1
                print("Count: %d\tx: %04d\tDic: %d\tWin?: %d\tNextbet: %04.8f\tCapital: %04.8f\tDeath: %d\t  BB: %08.8f Wagered: %d"% (countm,x,dic,win,nextbet,capital,death,biggestbet, wagered))
            
            #Stats and Preperation for next run
            wagered += previousbet
            previousbet = nextbet

    #Timer
    time = timer()-start
    #Final Stats

    #Converting

    print("Time: %04.2f\t Million Plays: %d\t T/CM: %02.4f\t" % (time, countm, time/countm,))

dobet()