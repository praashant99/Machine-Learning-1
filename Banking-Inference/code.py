# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
#Reading file
data=pd.read_csv(path)
#Code starts here
#data = pd.read_csv(path)
#print(data.head())
data_sample = data.sample(n = sample_size,random_state = 0)
#n = 30
#print(data_sample.head())

#Confidence Interval 
true_mean = data['installment'].mean()
print('True Mean is {}'.format(true_mean))
true_std = data['installment'].std()
true_std1 = data_sample['installment'].std()
print('Population Standard Deviation of the Installment Column is {}'.format(true_std))
sample_mean = data_sample['installment'].mean()
print('Sample mean of the Installment Column is {}'.format(sample_mean))
lower_limit = sample_mean - (z_critical*(true_std1/math.sqrt(sample_size)))
upper_limit = sample_mean + (z_critical*(true_std1/math.sqrt(sample_size)))
confidence_interval = [lower_limit, upper_limit]
print('Confidence Internal for sample mean is {}'.format(confidence_interval))

# CLT test by plotting
sample_sizes = np.array([20,50,100])
plt.figure(figsize = [12,7])
for sample_size in sample_sizes:
    lst = []
    for i in range(1000):
        df_new = data.sample(n = sample_size)
        lst.append(df_new['installment'].mean())
    sns.distplot(lst,hist = True,label = 'sample size {}'.format(sample_size))
    plt.legend()


#Small Business Interests
mean_intrate = data['int.rate'].apply(lambda x: float(x[:-1])).mean()
z_statistic_1, p_value_1 = ztest(data[data['purpose'] == 'small_business']['int.rate'].apply(lambda x: float(x[:-1])), value = mean_intrate, alternative = 'larger')
print('z_statistic_1 is {}'.format(z_statistic_1))
print('p_value_1 is {}'.format(p_value_1))

#Installment vs Loan Defaulting
mean_installment = data[data['paid.back.loan'] == 'Yes'].installment.mean()
x1 = data[data['paid.back.loan'] == 'No']['installment']
x2 = data[data['paid.back.loan'] == 'Yes']['installment']
value = np.mean(x1) - np.mean(x2)
print(value)
z_statistic_2, p_value_2 = ztest(x1,x2, value = 0)
print('z_statistic_2 is {}'.format(z_statistic_2))
print('p_value_2 is {}'.format(p_value_2))

#Purpose vs Loan Defaulting
new_df = data.groupby('paid.back.loan')['purpose'].value_counts().unstack()
chi2, p, dof, expected = chi2_contingency(new_df)
print('Chi-Square value is {}'.format(chi2))
print('Given Critical Value is {}'.format(critical_value))


