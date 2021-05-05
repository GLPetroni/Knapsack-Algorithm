#!/usr/bin/python3
import os,sys
#knapsack
def knapsack_d(W,N,values,weights):
    V = [[0 for x in range(W + 1)] for x in range(N + 1)] 
    for i,k in enumerate(range(N + 1)):
        w = 1
        for w in range(W + 1):
            if i == 0 or w == 0:
                V[i][w] = 0
            elif weights[i-1] <= w:
                V[i][w] = max(values[i-1]+V[i-1][w-weights[i-1]],V[i-1][w])
            else: 
                V[i][w] = V[i-1][w]
    return V[i][W],V

def getitem(sack,N,W,V,weights):
    items = []
    while(N>0 and W>0):
        if sack[N][W] != sack[N-1][W]:
            items.append(N)
            N-=1
            W-= weights[N]
        else:
            N -= 1
    items.reverse()
    return items 
if __name__=="__main__":
########################################################################################
#I used the following webpages to help create this:                                    #
# https://able.bio/rhett/python-read-a-file-line-by-line--116rey6                      #
# https://stackoverflow.com/questions/39921087/a-openfile-r-a-readline-output-without-n#
########################################################################################
    F = open("shopping.txt","r")
    T = int(F.readline().strip())
    for i in range(T):
        V = []
        W = []
        item = int(F.readline().strip())
        for j in range(item):
            p,w = map(int,F.readline().strip().split())
            V.append(p)
            W.append(w)
        MaxWeights = []
        people = int(F.readline().strip())
        for j in range(people):
            MaxWeights.append(int(F.readline().strip()))
        index = 0
        total_cost = 0
        items = []
        for x,j in enumerate(range(people)):
            max_value,sack = knapsack_d(MaxWeights[index],item,V,W) 
            items.append(getitem(sack,item,MaxWeights[index],V,W))
            total_cost = total_cost + max_value
            index+=1
        print('Test Case ',i+1)
        print('Total Price ',total_cost)
        for j in range(people):
            ints = [str(ind) for ind in items[j]]
            string = " ".join(ints)
            print(j+1,': ',string)
            
        
