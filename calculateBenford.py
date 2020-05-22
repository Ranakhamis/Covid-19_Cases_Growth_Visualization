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
from datetime import timedelta

df = pd.read_excel("COVID-19-geographic-disbtribution-worldwide.xlsx") 

print(df.info())

dropped= df.drop(['geoId','countryterritoryCode','deaths' ], axis=1, inplace= True)
print(dropped)
#print(df.head(10))
#print(df.shape)

print (type(False))

df['dateRep'] = pd.to_datetime(df['dateRep'])

#res = df[~(df['dateRep'] > '2020-04-25')]
res = df[(df['dateRep'] > '2020-04-25')]

print(res)

sub= df['cases']
#print(sub)

#Operations for adding new rows
def add_row(res):
    next_day = pd.to_datetime('today') + pd.DateOffset(days=1) 
    if res['dateRep'].max() < next_day:
        last_row =res.iloc[-1]
        last_row['dateRep'] = next_day #3'aleban hena badal ma7ott last_row ha7ott groupby ba3den    
        res['new']= last_row['dateRep'] + pd.to_timedelta(2, unit='d')      
        return res.append(last_row, ignore_index=True )
    return res
concatination = add_row(res)
print(concatination)



#===============================================================================================================================================




BENFORD_PERCENTAGES_first = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
BENFORD_PERCENTAGES_second = [0.1197, 0.1139, 0.1088, 0.1043, 0.1003, 0.0967, 0.0934, 0.0904, 0.0876, 0.0850]
    
def calculate(data):

    """
    Calculates a set of values from the numeric list
    input data showing how closely the first digits
    fit the Benford Distribution.
    Results are returned as a list of dictionaries.
    """
    results = []

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
            benford_frequency = len(sub) * BENFORD_PERCENTAGES_second[n]
            print (benford_frequency, "///","benford_frequency")   
            print ("=====================================================")    
            benford_frequency_percent = BENFORD_PERCENTAGES_second[n]
            print (benford_frequency_percent,"///", "benford_frequency_percent")
            print ("=====================================================")    
            difference_frequency = data_frequency - benford_frequency
            print (difference_frequency,"///","difference_frequency")     
            print ("=====================================================")    
            difference_frequency_percent = data_frequency_percent - benford_frequency_percent
            print (difference_frequency_percent,"///","difference_frequency_percent")     
            print ("=====================================================")   
	    #new_predicted_data= difference_frequency	
            results.append({"n": n,
                            "data_frequency":               data_frequency,
                            "data_frequency_percent":       data_frequency_percent,
                            "benford_frequency":            benford_frequency,
                            "benford_frequency_percent":    benford_frequency_percent,
                            "difference_frequency":         difference_frequency,
                            "difference_frequency_percent": difference_frequency_percent})

    return results

#===================================================



