# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

data['Gender'] = data['Gender'].str.replace('-','Agender')
data['Gender'].value_counts().plot(kind = 'bar')

data['Alignment'].value_counts()

dfnew = data[['Combat','Intelligence','Strength']]
dfnew.corr(method = 'spearman').iloc[0,1:]

benchmark = data['Total'].quantile(0.99)
super_best_names = list(data[data['Total'] >= benchmark]['Name'])

print(super_best_names)

# Code starts here



