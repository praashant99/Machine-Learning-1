# -*- coding: utf-8 -*-
"""Solution-v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D9rURBjUz6tB3vlUiU7rR200V9aPCAfA
"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

"""### Define the following functions as per the description, so that they can be called later to perform the tasks."""

# Remove correlated features

def remove_corelated_features(X_train,val):
    """ Function to remove the correlated features
    
    This function accepts the dataframe X_train,val which creates a correlation matix and removes 
    the correlated features based on certain threshold.
    
    Keyword arguments:
    X_train - Pandas dataframe which contains the independent features.
    val - Certain threshold value by which correlated features to be dropped.
    
    """
    # Create correlation matrix
    corr_matrix = X_train.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find index of feature columns with correlation greater than 0.75
    to_drop = [column for column in upper.columns if any(upper[column] > val)]
    print("Columns to be dropped: ",to_drop)
    
    return X_train.drop(to_drop,axis=1)

# check the distribution of the passed features
    
def cal_eval_metric(y_test, y_pred, metric):
    """  Check the distribution of the passed features
    
    This function will check for the metric passed(accuracy/precision/recall/f1/confusion matrix) 
    and return the required value.
    
    Keyword Arguments:   
    y_test: actual target values
    y_pred: predicted target values
    metric: the metric to be calculated
    
    """
    if metric == 'accuracy':
        score = accuracy_score(y_test, y_pred)

    elif metric == 'precision':
        score = precision_score(y_test, y_pred)
    
    elif metric == 'recall':
        score = recall_score(y_test, y_pred)
    
     
    elif metric == 'f1':
        score = f1_score(y_test, y_pred)
        
    elif metric == 'roc_auc':
        score = roc_auc_score(y_test, y_pred)
        
    else:
        print("Please enter proper score metric.")

    return score

"""### Read the dataset. Take a look at the dataset. 

* Check the data types present in the dataframe.
* Call the num_and_cat_columns() with train as the parameter and store the results.
* Are there any missing values? Are there any Outliers? How do you want to treat them?

"""

train = pd.read_csv("train.csv")
print(train.head())

"""### Visualize the data

- Check for the categorical & continuous features. 
- Check out the best plots for plotting between categorical target and continuous features and try making some inferences from these plots.
- Clean the data and apply some data preprocessing techniques
"""

# Now, check the correlation. 
# For highly correlated features adds no extra information to the model, we will drop the columns that are highly correlated with others.
# Call remove_correlated_features() with the threshold value 0.75 to be dropped.

# You can play with different threshold value and see how it affects on the score.

train = remove_corelated_features(train, 0.75)

"""### Model building

- Separate the features and target and then split the train data into train and validation set.
- Now let's come to the actual task, using linear regression, predict the `Total Compensation`. 
- Try improving upon the `r2_score` (R-Square) using different parameters that give the best score.


"""

# Split the data into train and test
X = train.drop(columns = ['loan_status'])
y = train[['loan_status']]

print(y['loan_status'].unique())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Now let's come to the actual task, using logistic regression to predict the loan_status. 
# fit the model and predit the target values

#Instantiate logistic regression model
L_regressor=LogisticRegression()

# fit the model on train data
L_regressor.fit(X_train, y_train)

# predict the result
y_pred =L_regressor.predict(X_test)


# We will check the model accuracy using `accuracy score`, `precision score`, `recall score`, and `f1 score`. 
# To see your model's performance, call the cal_eval_metric() with respective parameters.

accuracy= cal_eval_metric(y_test,y_pred,  'accuracy')
precision = cal_eval_metric(y_test,y_pred,  'precision')
recall = cal_eval_metric(y_test,y_pred,  'recall')
f1 = cal_eval_metric(y_test,y_pred,  'f1')
roc_auc= cal_eval_metric(y_test,y_pred,  'roc_auc')

print("Accuracy Score: ", accuracy)
print("Precision Score: ", precision)
print("Recall Score: ", recall)
print("F1 Score: ", f1)
print("Roc Auc Curve: ", roc_auc)




# Lets apply a feature selection technique(Recursive Feature Elimination test)to see whether we can increase our score.
# Create a list of the number of features and call transform the dataset to train the model.


model = LogisticRegression()

high_score = 0  
nof = 0
nof_list=[5,10,15,20,25]
    
for n in nof_list:
    test_ = RFE(model,n)
    X_train = test_.fit_transform(X_train,y_train)
    X_test = test_.transform(X_test)
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    score = f1_score(y_pred,y_test)
    
    if score > high_score:
        high_score = score
        nof = n
        test_best = test_ # store the model with best score to make prediction on the test data
        
print("Highest F1 Score is:",high_score, "with features=",nof)

"""### Prediction on the test data and creating the sample submission file.

- Load the test data and store the `Id` column in a separate variable.
- Perform the same operations on the test data that you have performed on the train data.
- Create the submission file as a `csv` file consisting of the `Id` column from the test data and your prediction as the second column.
"""

# Code Starts here
# Prediction on test data

# Read the test data
test = pd.read_csv('test.csv')

# Storing the id from the test file
id_ = test['Id']

# Dropping the same columns from the test data and applying same transformation

test = test.drop(['funded_amnt', 'installment', 'grade', 'collection_recovery_fee', 'total_rev_hi_lim'],axis=1)

test = test_best.transform(test)

# Predict on the test data
y_pred_test = model.predict(test)
y_pred_test = y_pred_test.flatten()

# Create a sample submission file
sample_submission = pd.DataFrame({'Id':id_,'loan_status':y_pred_test})

# Convert the sample submission file into a csv file
# sample_submission.to_csv('sample_submission.csv',index=False)

# Code ends here

