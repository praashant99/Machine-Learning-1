# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(path)
p_a = df[df.fico > 700].shape[0]/df.shape[0]
p_b = df[df.purpose == 'debt_consolidation'].shape[0]/df.shape[0]
df1 = df[df.purpose == 'debt_consolidation']
p_a_b = df1[df1.fico > 700].shape[0]/df1.shape[0]
result = (p_a_b == p_a)
print('result is {}'.format(result))

prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
new_df = df[df['paid.back.loan'] == 'Yes']
probs_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
bayes = round((probs_pd_cs * prob_lp) / prob_cs , 4)
#bayes = (probs_pd_cs * prob_lp) / prob_cs 
#print(round(bayes,4))
print('bayes value is {}'.format(bayes))

df.purpose.value_counts().plot(kind = 'bar')
df1 = df[df['paid.back.loan'] == 'No']
df1.purpose.value_counts().plot(kind = 'bar')
print('Shape of df1 is {}'.format(df1.shape))

inst_median = df.installment.median()
inst_mean = df.installment.mean()
df.installment.plot.hist()
df['log.annual.inc'].plot.hist()
plt.axvline(x = inst_mean)
plt.axvline(x = inst_median)


