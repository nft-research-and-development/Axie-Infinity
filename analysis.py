import csv
import pandas as pd
import numpy as np

import statsmodels.api as sm

from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.cluster import KMeans


import matplotlib.pyplot as plt


data = pd.read_excel (r'/mnt/c/Users/Runxin Li(Sally)/Desktop/S22/URP/axie_query.xls',sheet_name="axie_query") 
df = pd.DataFrame(data, 
	columns= ['id','class','birthDate','level','breedCount','price','hp','speed','skill','morale','random_children_id'])
df['class'].replace(['Aquatic','Beast','Bird','Bug','Dawn','Dusk','Mech','Plant','Reptile'],
	[0,1,2,3,4,5,6,7,8],inplace=True)



'''
axie_id = np.array(df['id'])
print(axie_id.shape)

axie_id.reshape(-1,1)
print(axie_id.shape)

axie_id= axie_id.reshape(-1,1)
print(axie_id.shape)

regr = LinearRegression()
regr.fit(data, data)
'''
'''
###OLS +Pearsons + Spearmans TEST
#relationship between breedcount and prices
X = df["breedCount"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('breedcount OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)

#relationship between birthdate and prices
X = df["birthDate"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('birthdate OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)



#relationship between class and prices(categorical variable and needs to be turned into numerical values)
X = df["class"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('class OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)





#relationship between breedcount,level and prices
X = df[["breedCount","level"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('breedcount+level OLS & no Pearsons or Spearmans')
print(model.summary())


#relationship between birthdate and prices
X = df["hp"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('hp OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)


#relationship between birthdate and prices
X = df["speed"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('speed OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)

#relationship between birthdate and prices
X = df["skill"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('skill OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)


#relationship between birthdate and prices
X = df["morale"]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('morale OLS')
print(model.summary())

corr, _ = pearsonr(X, y)
print('Pearsons correlation: %.3f' % corr)

corr, _ = spearmanr(X, y)
print('Spearmans correlation: %.3f' % corr)


#relationship between 4 statistics and prices
X = df[["skill","hp","speed","morale"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(4) OLS & & no Pearsons or Spearmans')
print(model.summary())


#relationship between breedcount, class and prices
X = df[["breedCount","class"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(2) OLS & & no Pearsons or Spearmans')
print(model.summary())


#relationship between breedcount, skill and prices
X = df[["breedCount","skill"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(2) OLS & & no Pearsons or Spearmans')
print(model.summary())



#relationship between breedcount, speed and prices
X = df[["breedCount","speed"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(2) OLS & & no Pearsons or Spearmans')
print(model.summary())


#relationship between breedcount, speed, skill and prices
X = df[["breedCount","speed","skill"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(3) OLS & & no Pearsons or Spearmans')
print(model.summary())



#relationship between traits and prices
X = df[["breedCount","class","hp","speed","skill","morale"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(3) OLS & & no Pearsons or Spearmans')
print(model.summary())


#relationship between speed, skill and prices
X = df[["speed","skill"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(3) OLS & & no Pearsons or Spearmans')
print(model.summary())

#relationship between speed, skill, class and prices
X = df[["speed","skill","class"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(3) OLS & & no Pearsons or Spearmans')
print(model.summary())

#relationship between speed, skill, class and prices
X = df[["level"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(3) OLS & & no Pearsons or Spearmans')
print(model.summary())

'''
#relationship between speed, skill, class and prices
X = df[["speed","skill","level"]]
y = df["price"]

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statistics
print('stats(3) OLS & & no Pearsons or Spearmans')
print(model.summary())