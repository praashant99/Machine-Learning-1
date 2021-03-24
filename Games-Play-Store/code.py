# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.preprocessing import Imputer




#Loading the data
data=pd.read_csv(path)

#Code starts here
data = data[data['Rating'] <= 5.0]
data.drop(4868, axis = 0, inplace = True)
data['Current Ver'].replace(np.nan, 'Varies with device', inplace = True)
data['Android Ver'].replace(np.nan,'4.1 and up',inplace = True)

data.Genres = data.Genres.apply(lambda x: str(x).split(';')[0])
#data['Last Updated'] = pd.to_datetime(data['Last Updated'])
data.set_index('App',inplace = True)

#data.Installs = data.Installs.str.replace(',','')
#data.Installs = data.Installs.apply(lambda x: float(x[:-1]))

mean_imputer = Imputer(strategy = 'mean')
mode_imputer = Imputer(strategy = 'mode')

mean_imputer.fit(data[['Rating']])
data['Rating'] = mean_imputer.transform(data[['Rating']])

data.Price = [float(x[1:]) if (len(x) > 1) else float(x) for x in data.Price]








