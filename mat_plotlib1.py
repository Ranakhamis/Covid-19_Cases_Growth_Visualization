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
plt.show()

#geoId countryterritoryCode
