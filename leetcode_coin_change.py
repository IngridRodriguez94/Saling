# -*- coding: utf-8 -*-
"""Leetcode_coin_change.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1no7yB_s_4l11-bHRS1C_DwykJJZl5Eg9
"""

import math

#Grid Approach
#Restrictions 1 < amount <100
def makeCoinChange_US(denominations, amount):
  denominations.sort(reverse=True)
  lista_acumulado=[]
  lista_total=[]
  #-We will try with the different coin pointed out
  for coin in denominations:
    #If there are no residuals, automatically I return the coin and the result of the amount/divided by the coin
    #The coin is divisible or not
    if amount % coin ==0:
      acumulado=amount/coin
      lista_acumulado=[coin,acumulado]
      lista_total.append(lista_acumulado)
      return lista_total
    elif amount % coin !=0:
      #If there are residuals, I get the result of the amount/divided by the coin using mathfloor
      acumulado=(amount//coin)
      #I assign the coin and the result above in a final list
      lista_acumulado=[coin,acumulado]
      lista_total.append(lista_acumulado)

      #Now, the amount left will be the substraction of the current amount and the total of acumulado=(amount/coin)*coin
      amount=amount-(acumulado*coin) #Equivalent to amount%coin
      #amount=amount%coin
  
  return int(lista_total)

#denominations = [25,10,5,1]
denominations = [1,5,10,25]
amount=97

#Testing
makeCoinChange_US(denominations,amount)

#Find a general solution using dynamic prograaming that works for all kinds of denominations

def coinChange(coins, amount):
    # Initialize an array arr1 with the length of amount + 1, 
    # and set all values to positive infinity except arr1[0] to 0
    arr1 = [float('inf')] * (amount + 1)
    arr1[0] = 0
    
    # Loop through all amounts from 1 to amount
    for i in range(1, amount + 1):
        # Loop through all coins in the coins array
        for coin in coins:
            # If the current coin is less than or equal to the current amount
            if coin <= i:
                # Update the value of arr1[i] with the minimum of its current value
                # and arr1[i - coin] + 1, where arr1[i - coin] + 1 represents the
                # minimum number of coins needed to make the current amount minus
                # the current coin, plus 1 for the current coin
                arr1[i] = min(arr1[i], arr1[i - coin] + 1)
                
    # If arr1[amount] is still equal to positive infinity, it means that it is not
    # possible to make the target amount with the given set of coins, so return -1
    if arr1[amount] == float('inf'):
        return -1
    else:
        # Otherwise, return arr1[amount], which is the minimum number of coins needed
        # to make the target amount
        return arr1[amount]

coinChange(denominations,amount)