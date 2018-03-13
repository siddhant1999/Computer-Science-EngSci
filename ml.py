import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
#print df
#print "Done"
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
#df = dataframe
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
#HL_PCT is the high-low percentage

df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#PCT_change is the percent change (this is a good indication of the volitility)
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
#df['label'] = df[forecast_col]
#length of df times 0.01 ceilinged 
#0.01 represents 1% of the dataframe (meaning we are predicting 1% out)
#print (df.head(10))
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
#features
y = np.array(df['label'])
#labels

X = preprocessing.scale(X)

#X = X[:-forecast_out+1]
df.dropna(inplace=True)
y= np.array(df['label'])
print (len(X), len(y))