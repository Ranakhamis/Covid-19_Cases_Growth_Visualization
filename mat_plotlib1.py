#!/home/rana/anaconda3/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import matplotlib.animation as animation
from scipy.stats import linregress


data = pd.read_excel("COVID-19-geographic-disbtribution-worldwide.xlsx") 

#print(data.head(1000))
#print(data.info())
#sorted_hills = dataframe.sort_values(by=['Height'], ascending=False)

print(data.drop(['geoId','countryterritoryCode' ], axis=1, inplace= True))
print(data.head(10))

print(data.shape)

print (type(False))

#boolean = []
#for length in data.dateRep:
#    if length >= 2020-04-25
#       booleans.append(True)
#   else:
#	booleans.append(False)

#boolean[0:5]

data['dateRep'] = pd.to_datetime(data['dateRep'])

res = data[~(data['dateRep'] < '2020-04-25')]

print(res)

plt.show()


