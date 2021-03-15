# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.head())
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.head())
banks = bank.drop(['Loan_ID'],axis = 1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode,inplace = True)
print(banks.isnull().sum())
avg_loan_amount = banks.pivot_table(index = ['Gender','Married','Self_Employed'], values = 'LoanAmount',aggfunc = np.mean)
print(avg_loan_amount)
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = loan_term[loan_term >= 25].count()
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()



