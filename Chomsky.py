# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:01:19 2021

"""
def listPrint(listeN):
    
    listeN.reverse()
    liste=[]
    for line in listeN:
        liste.append(" ".join(line))

    for i in liste:
        print (i)

inputString= "aabbb"
n= len(inputString)
listN=[ ["-"]*(n) for i in range(n)]

# Rule List
listR=[["S","A","S"],["S","A","b"],["S","a","S"],["S","a","b"],["A","S","S"],["A","b","b"],["A","b","S"],["A","S","b"],["B","A","S"]]


for i in range(n):
    listN[i][i] = inputString[i] #initial condition
   

for s in range (n):
    for i in range ((n-s)+1):
        for k in range(i,i+s):

            for j in range(len(listR)): #checks all the rules
                
                if(k < len(listN) and i+s < len(listN)):
                    if(listR[j][1]==listN[i][k]):    
                        if(listR[j][2]==listN[k+1][i+s]):
                            
                            if(listN[i][i+s]=="-"):
                                print(f"{listN[i][k]} at N[{i}][{k}] and {listN[k+1][i+s]} at N[{k+1}][{i+s}] is equal to rule {listR[j][0]}->{listR[j][1]}{listR[j][2]}")
                                listN[i][i+s]=listR[j][0]
                                print(f"{listR[j][0]} is added to N[{i}][{i+s}]")
                                print("")
                                

                                                    
if(listN[0][n-1]==listR[0][0]):
    listPrint(listN)
    print(f"Last index is the start symbol {listR[0][0]}")
    print("String is accepted.")
    

    
else:
    listPrint(listN)
    print(f"Last index is {listN[1][n-1]} but the start symbol is {listR[0][0]}")
    print("String is not accepted.")


    