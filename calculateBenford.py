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
from datetime import datetime, date, time, timedelta
import time

df = pd.read_excel("COVID-19-geographic-disbtribution-worldwide.xlsx",parse_dates=['dateRep']) 

dropped= df.drop(['geoId','countryterritoryCode','deaths','popData2018' ], axis=1, inplace= True)
print (type(False))

df['dateRep'] = pd.to_datetime(df['dateRep'])

res = df[(df['dateRep'] > '2020-04-25')] #res = df[~(df['dateRep'] > '2020-04-25')]
sub= df['cases']

#Adding new dataframe for new rows concatination
df2 = pd.DataFrame( columns = ['dateRep',  'day',  'month',  'year',  'cases' ,'countriesAndTerritories','continentExp'])

#Operations for adding new rows with future dates
def add_rows(df):
                         
    numdays = 10
    #dateList = []
    today = datetime.today()	
    base = today #- number
    #from 10/5 till today 
    date_list= [base + timedelta(days=x) for x in range(numdays)] 
    df2['dateRep']=date_list 
    result= df.append(df2, ignore_index=True )	 
    return result

concatination= add_rows(df)
#concatination.to_excel("output.xlsx")  
print (concatination)

def repeat_rows(df):
    countries_counter= len(df['countriesAndTerritories'].unique().tolist())	
    for x in range(countries_counter):
            repeat = concatination.groupby('countriesAndTerritories')
    return repeat

show= repeat_rows(df)
print(show)	
 
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



