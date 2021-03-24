## **Problem statement**

You are a die hard Lego enthusiast wishing to collect as many board sets as you can. But before that you wish to be able to predict the price of a new lego product before its price is revealed so that you can budget it from your revenue. Since (luckily!), you are a data scientist in the making, you wished to solve this problem yourself. This dataset contains information on lego sets scraped from lego.com. Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. Your aim is to build a linear regression model to predict the price of a set. The snapshot of the data, you will be working on :

## data

You can see that some of the features of review_difficulty, theme_name and Country Name in the data are textual in nature. Don't worry, we have made things simple for you with some behind-the-scenes data preprocessing. We have also modified the feature of age. You will be learning about all these preprocessing techinques in a later concept. For now let us concentrate on getting those Lego sets in your hands soon. :)

## new data

Your aim is to build a linear regression model to predict the price of a set.

## About the dataset

A zipped file containing the following items is given:

train.csv : The data file train.csv contains the 8582 instances with the 11 features including the target feature. 

test.csv" : The datafile test.csv contains the 3679instances with the 10 features excluding the target feature. 

sample_submission.csv : Explained under the Submission sub-heading 

LCDataDictionary.csv: The file contains data dictionary(Dictionary explaining what each feature of the dataset means) of the LEGO dataset 

LEGO_Dilemma_student_template.ipynb : A template notebook explaining the task breakdown to solve the given problem statement (Learners are recommended to use it)
Submission

After training the model on train.csv data, the learner has to predict the target feature of the test.csv data using the trained model. The learner has to then submit a csv file with the predicted feature. Sample submission file(sample_submission.csv) is given to you as a reference to the format expected when you submit

## Evaluation metrics

For this particular dataset we are using r2 score as the evaluation metric. Submissions will be evaluated based on r2 score

Your r2_score score	Points earned for the Task
r2_score>0.77	100% of the available points
0.77 < r2_score < 0.74	80% of the available points
0.74 < r2_score < 0.70	70% of the available points
r2_score <= 0.70	No points earned


## Outcomes

The main objective of this task is to provide you with an open field where you can practice and work your way with a dataset end to end without any restrictions from our side. So feel free to play around the model until you arrive at your best solution. In this project, you will apply the following concepts:

Train-test split
Correlation between the features
Linear Regression
MSE and R-Square Evaluation Metrics 

After completing this project, you will have the better understanding of how to build a linear regression model.
