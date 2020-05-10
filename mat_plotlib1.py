#!/home/rana/anaconda3/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import sys
import benfordslaw as bl
import matplotlib.animation as animation
import collections
import random
import benfordslaw
import random

df = pd.read_excel("COVID-19-geographic-disbtribution-worldwide.xlsx") 

#print(data.head(1000))
print(df.info())


print(df.drop(['geoId','countryterritoryCode' ], axis=1, inplace= True))
print(df.head(10))

print(df.shape)

print (type(False))

df['dateRep'] = pd.to_datetime(df['dateRep'])

res = df[~(df['dateRep'] < '2020-04-25')]

print(res)

sub= df['cases']
print(sub)
plt.show()

#-----------------------------------------------------------------------
#trial = data.apply(BenfordsLaw)
#trial= data.apply(BenfordsLaw, axis=1)
#print(trial.head(3)) 

#------------------------------------------------------------

BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def main():
    
    
    #def __init__(self): 

#        self.String1 ="Benfords Law"

    #def calculate(df):

        """
        Calculates a set of values from the numeric list
        input data showing how closely the first digits
        fit the Benford Distribution.
        Results are returned as a list of dictionaries.
        """

     #   results = []

first_digits = list(map(lambda n: str(n)[0], sub))
first_digit_frequencies = collections.Counter(first_digits)
print (first_digit_frequencies)

for n in range(1, 10):

    data_frequency = first_digit_frequencies[str(n)]        
    print (data_frequency, "data_frequency") 
    print ("=====================================================")    
    data_frequency_percent = data_frequency / len(sub)  
    print (data_frequency_percent,"///","data_frequency_percent")    
    print ("=====================================================")    
    benford_frequency = len(sub) * BENFORD_PERCENTAGES[n]
    print (benford_frequency, "///","benford_frequency")   
    print ("=====================================================")    
    benford_frequency_percent = BENFORD_PERCENTAGES[n]
    print (benford_frequency_percent,"///", "benford_frequency_percent")
    print ("=====================================================")    
    difference_frequency = data_frequency - benford_frequency
    print (difference_frequency,"///","difference_frequency")     
    print ("=====================================================")    
    difference_frequency_percent = data_frequency_percent - benford_frequency_percent
    print (difference_frequency_percent,"///","difference_frequency_percent")     
    print ("=====================================================")   
main()
    


