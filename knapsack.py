#!/usr/bin/python3
import time
from random import seed
from random import randint

def knapsack_r(W,N,values,weights):
    if N==0 or W==0:
        return 0
    if (weights[N-1] > W):
        return knapsack_r(W, N-1,values,weights)
    else:
        return max(values[N-1]+knapsack_r(W-weights[N-1],N-1,values,weights), knapsack_r(W,N-1,values,weights))  


def knapsack_d(W,N,values,weights):
    V = [[0 for x in range(W + 1)] for x in range(N + 1)] 
    for i in range(N + 1):
        w = 1
        for w in range(W + 1):
            if i == 0 or w == 0:
                V[i][w] = 0
            elif weights[i-1] <= w:
                V[i][w] = max(values[i-1]+V[i-1][w-weights[i-1]],V[i-1][w])
            else: 
                V[i][w] = V[i-1][w]
        
    return V[i][W]

if __name__=="__main__":
    seed(1)
    rec_times = []
    dp_times = []
    #generate test cases
    x=0
    dpN = [100,150,200,250,300,350,400]
    dpW = 1200 
    N = [15,20,25,30,35,40,45]
    W = 100
    for i in N:
        values = []
        weights = []
        dpvalues = []
        dpweights = []
        for j in range(i):
            tmp = randint(1,i-1)
            values.append(tmp) 
        for k in range(W):
            tmp = randint(1,25)
            weights.append(tmp)
        for n in range(dpN[x]):
            tmp = randint(1,dpN[x]-1)
            dpvalues.append(tmp) 
        for m in range(dpW):
            tmp = randint(1,40)
            dpweights.append(tmp)
        t = time.process_time()
        rec_max = knapsack_r(W,i,values,weights)
        run_time = time.process_time() - t
        d = time.process_time()
        dp_max = knapsack_d(dpW,dpN[x],dpvalues,dpweights)
        dp_time = time.process_time()-d
        print('N: ',i,'W: ',W,' rec_time=',run_time,' rec_max=',rec_max,' dp_time=',float(dp_time),' dp_max=',dp_max)
        x+=1
    
