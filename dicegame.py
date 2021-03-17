import numpy as np
from timeit import default_timer as timer

def dobet():
    # Main Variables
    base = 10
    chance = 1000
    balance = 1
    multiplier = 113
    chan = int(chance/100)

    winmulti = int((99/chan*100))
    
    # Placeholders
    previousbet = base
    nextbet = base
    basebalance = balance
    eight = 10000000

    # Stats
    win = 0
    biggestbet = 0
    smallestbet = 0
    smallestbalance = 0
    profit = 0.00
    count = 0
    countm = 0
    death = 0

    #Test_data
    size = 100   #1
    rng = np.random.default_rng()
    test_data = rng.integers(1, high=10000, size=size)

    start = timer()

    for x in test_data:
        #Definition
        count += 1
        if x<chance:
            win = 1 
        else:
            win = 0

        if win==1: 
            balance += (previousbet*winmulti)/100
            balance = int(balance/100)
        else:
            balance = (balance*100-previousbet*100)
            balance = int(balance/100)

        if win:
            profit = int((profit*100 + previousbet*winmulti)/100)
            nextbet = base
            if nextbet < base:
                nextbet = previousbet
        else:
            profit = int((profit*100 - previousbet*100)/100)
            nextbet = int((previousbet*100*multiplier)/100/100)

        if nextbet>biggestbet:
            biggestbet=nextbet
        if balance<smallestbalance:
            smallestbalance = balance

        #if balance<0:
        #   death +=1
        #    nextbet=base
        #    balance = basebalance

        if count % 1 == 0:
            countm +=1
            print("Count: %d\tx: %04d\tChance: %d\tWin?: %d\tNextbet: %04.8f\tBalance: %02.8f\tDeath: %d\t  BB: %04.8f\t SB: %04.8f" % (countm,x,chance,win,nextbet/eight,balance/eight,death,biggestbet/eight,smallestbalance/eight))
            
        #Stats and Preperation for next run
        previousbet = nextbet

    time = int(timer()-start)
    print("Time: %04.2f\t Million Plays: %d\t T/CM: %02.4f\t" % (time, countm, time/countm,))

dobet()