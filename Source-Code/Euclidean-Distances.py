#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Sep 29 10:27:04 2022
@author: moeezkhan
"""

import pandas as pd
import numpy as np
from scipy.spatial import distance
import timeit  


''' Use the default value of numRows (None) to read *all* rows '''

# Read -- import data
def readData(numRows = None):
    
    inputCols = ["Alcohol", 
                 "Malic Acid", 
                 "Ash", 
                 "Alcalinity of Ash", 
                 "Magnesium", 
                 "Total Phenols", 
                 "Flavanoids", 
                 "Nonflavanoid Phenols", 
                 "Proanthocyanins", 
                 "Color Intensity", 
                 "Hue", 
                 "Diluted", 
                 "Proline"]
    
    outputCol = 'Class'
    
    colNames = [outputCol] + inputCols  #concatenate two lists into one
        
    wineDF = pd.read_csv("data/wine.data", header = None, names = colNames, nrows = numRows)
    
    return wineDF, inputCols, outputCol



#===================== Calculations Begin (Steps#1,2,3,4,5) ===================

# Function#1 -- DONE 
def euclideanDist1(s1, s2):
    
    combinedSeries = s1 - s2
    squaredSum = 0
    
    for value in combinedSeries:
        squaredSum += value ** 2
        
    return squaredSum ** (1/2)
        


# Function#2 -- DONE
def euclideanDist2(p1, p2):
    
    validP1Series = pd.Series( range(14) )
        
    squaredDifferenceSum = validP1Series.map( lambda value : ( p1.iloc[value] - p2.iloc[value] ) ** 2 )
    
    return squaredDifferenceSum.sum() ** (1/2)
    


# Function#3 -- DONE
def euclideanDist3(s1, s2):
    
    squaredSum = (s1 - s2) ** 2
            
    return squaredSum.sum() ** (1/2)



# Function#4 -- DONE
def euclideanDist4(p1, p2):  
    return np.linalg.norm(p1 - p2)
    


# Function#5 -- DONE
def euclideanDist5(s1, s2):
    return distance.euclidean(s1, s2)



#======================== Testing Begins (Steps#6,7,8,9) ======================


#Functions for Step 8 - Increasing attibutes
def addRandomCols(df, numNewCols):
    newCols = pd.Series(['rndC'+str(i) for i in range(0, numNewCols)]) 
    newCols.map(lambda colName: addRandomCol(colName, df))


    
def addRandomCol(colName, df):
    df.loc[:, colName] = np.random.randint(-100, 100, df.shape[0])



# Main - Intialise Series Objects
def main():
    df, inputCols, outputCol = readData(3)

    a = df.iloc[0, :]
    b = df.iloc[1, :]
    c = df.iloc[2, :]
    
    
    
# Step 6) Timing! =============================================================

#     startTime1 = timeit.default_timer()
#     print()
#     print("================ Func1")
#     print(euclideanDist1(a, b))
#     print(euclideanDist1(a, c))
#     print(euclideanDist1(b, c))
#     
#     print(str(timeit.default_timer() - startTime1) + " seconds")
#     
#     startTime2 = timeit.default_timer()
#     print()
#     print("================ Func2")
#     print(euclideanDist2(a, b))
#     print(euclideanDist2(a, c))
#     print(euclideanDist2(b, c))
#     print(str(timeit.default_timer() - startTime2) + " seconds")
#     
#     startTime3 = timeit.default_timer()
#     print()
#     print("================ Func3")
#     print(euclideanDist3(a, b))
#     print(euclideanDist3(a, c))
#     print(euclideanDist3(b, c))
#     print(str(timeit.default_timer() - startTime3) + " seconds")
# 
# 
#     startTime4 = timeit.default_timer()
#     print()
#     print("================ Func4")
#     print(euclideanDist4(a, b))
#     print(euclideanDist4(a, c))
#     print(euclideanDist4(b, c))
#     print(str(timeit.default_timer() - startTime4) + " seconds")
# 
#     
#     startTime5 = timeit.default_timer()
#     print()
#     print("================ Func5")
#     print(euclideanDist5(a, b))
#     print(euclideanDist5(a, c))
#     print(euclideanDist5(b, c))
#     print(str(timeit.default_timer() - startTime5) + " seconds")
# 
#     print()
#     print("Fastest Algorithm: Func3")
# =============================================================================




# Step 7) Timing! Again =======================================================

#     startTime1 = timeit.default_timer()
#     print()
#     print("================ Func1")
#     for i in range(1000):
#         euclideanDist1(a, b)
#         euclideanDist1(a, c)
#         euclideanDist1(b, c)
#     print(str(timeit.default_timer() - startTime1) + " seconds")
#     
#     
#     startTime2 = timeit.default_timer()
#     print()
#     print("================ Func2")
#     for i in range(1000):
#         euclideanDist2(a, b)
#         euclideanDist2(a, c)
#         euclideanDist2(b, c) 
#     print(str(timeit.default_timer() - startTime2) + " seconds")
#     
#     
#     startTime3 = timeit.default_timer()
#     print()
#     print("================ Func3")
#     for i in range(1000):
#         euclideanDist3(a, b)
#         euclideanDist3(a, c)
#         euclideanDist3(b, c) 
#     print(str(timeit.default_timer() - startTime3) + " seconds")
# 
# 
#     startTime4 = timeit.default_timer()
#     print()
#     print("================ Func4")
#     for i in range(1000):
#         euclideanDist4(a, b)
#         euclideanDist4(a, c)
#         euclideanDist4(b, c)
#     print(str(timeit.default_timer() - startTime4) + " seconds")
# 
#     
#     startTime5 = timeit.default_timer()
#     print()
#     print("================ Func5")
#     for i in range(1000):
#         euclideanDist5(a, b)
#         euclideanDist5(a, c)
#         euclideanDist5(b, c)
#     print(str(timeit.default_timer() - startTime5) + " seconds")
# 
#     print()
#     print("Slowest to Fastest Algorithm:")
#     print("Slowest: Func2")
#     print("Func3")
#     print("Func4")
#     print("Func1")
#     print("Fastest: Func5")
# =============================================================================
    
    
    
    
# Step 8) Timing! One More Time ===============================================
    
#     addRandomCols(df, 100)
# 
#     startTime1 = timeit.default_timer()
#     print()
#     print("================ Func1")
#     for i in range(1000):
#         euclideanDist1(a, b)
#         euclideanDist1(a, c)
#         euclideanDist1(b, c)
#     print(str(timeit.default_timer() - startTime1) + " seconds")
#     
#     
#     startTime2 = timeit.default_timer()
#     print()
#     print("================ Func2")
#     for i in range(1000):
#         euclideanDist2(a, b)
#         euclideanDist2(a, c)
#         euclideanDist2(b, c) 
#     print(str(timeit.default_timer() - startTime2) + " seconds")
#     
#     
#     startTime3 = timeit.default_timer()
#     print()
#     print("================ Func3")
#     for i in range(1000):
#         euclideanDist3(a, b)
#         euclideanDist3(a, c)
#         euclideanDist3(b, c) 
#     print(str(timeit.default_timer() - startTime3) + " seconds")
# 
# 
#     startTime4 = timeit.default_timer()
#     print()
#     print("================ Func4")
#     for i in range(1000):
#         euclideanDist4(a, b)
#         euclideanDist4(a, c)
#         euclideanDist4(b, c)
#     print(str(timeit.default_timer() - startTime4) + " seconds")
# 
#     
#     startTime5 = timeit.default_timer()
#     print()
#     print("================ Func5")
#     for i in range(1000):
#         euclideanDist5(a, b)
#         euclideanDist5(a, c)
#         euclideanDist5(b, c)
#     print(str(timeit.default_timer() - startTime5) + " seconds")
#     
#     print()
#     print("Slowest to Fastest Algorithm:")
#     print("Slowest: Func2")
#     print("Func3")
#     print("Func1")
#     print("Func4")
#     print("Fastest: Func5")
# =========================================================================




# Step 9) Putting It All Together =============================================
#
#   Function4 (Using NumPy linalg) and Function5 (Using SciPy distnace) 
#   seem to have a very low rate of growth, since their elapsed times have 
#   changed minimally by increasing the number of attributes

#   The average increase in elapsed time for both these algorithims = 0.002 seconds
#
#   Although Function4 and Function5 have the lowest rate of growth
#   Function1's (Using iteration) elapsed times seems to have changed minimally as well
#   The average increase in elapsed time for this algorithim = 0.009 seconds 
#
# =============================================================================


#Calling test04
    print()
    print("================ Test04")
    test04(a, b, c)    



# Calculation Testing Function
def test04(a, b, c):
    df, inputCols, outputCol = readData(3)

    print(euclideanDist1(a, c))
    print(euclideanDist2(a, c))
    print(euclideanDist3(a, c))
    print(euclideanDist4(a, c))
    print(euclideanDist5(a, c))



#Calling main() for testing purposes
main()
