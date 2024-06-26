import os
import mlflow
import argparse
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#load the dataset
dataset = pd.read_csv('train_loan.csv')
numerical_cols = dataset.select_dtypes(include=['int64','float64']).columns.tolist()
categorical_cols = dataset.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('Loan_Status')
categorical_cols.remove('Loan_ID')


#fill categorical column missing values with mode
for col in categorical_cols:
    dataset[col].fillna(dataset[col].mode()[0] , inplace=True)


#fill numerical column missing values with median
for col in numerical_cols:
    dataset[col].fillna(dataset[col].median() , inplace=True)


#remove outliers
dataset[numerical_cols] = dataset[numerical_cols].apply(lambda x: x.clip(*x.quantile(0.05,0.95)))


#Log transformation
dataset['LoanAmount'] = np.log(dataset['LoanAmount'])
dataset['TotalIncome'] = dataset['ApplicantIncome'] + dataset['CoapplicantIncome']
dataset['TotalIncome'] = np.log(dataset['TotalIncome'])

#Drop Applicant and coApplicant
dataset = dataset.drop(['ApplicantIncome','CoapplicantIncome'],axis = 'columns')

#Label encoding categorical variable
for col in categorical_cols:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])

#Encode target column
dataset['Loan_Status'] = le.fit_transform(dataset['Loan_Status'])

#Train test Split
X = dataset.drop(['Loan_Status','Loan_ID'] , axis = 'columns')
y = dataset.Loan_Status

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7,random_state=123)

#Random Forest
rf = RandomForestClassifier()
param_grid_forest ={

}
grid_forest = GridSearchCV(
    estimator = rf,
    param_grid = param_grid_forest,
    cv = 5,
    score = 'accuracy'
)
model_forest = grid_forest.fit(X_train,y_train)

#Logistic
lr = LogisticRegression()
param_grid_log ={

}
grid_log = GridSearchCV(
    estimator = lr,
    param_grid = param_grid_log,
    cv = 5,
    score = 'accuracy'
)

model_log = grid_log.fit(X_train,y_train)

#Decision Tree
dt = DecisionTreeClassifier()
param_grid_tree = {

}
grid_tree = GridSearchCV(
    estimator = dt,
    param_grid = param_grid_tree,
    cv = 5,
    score = 'accuracy'
)

model_tree = grid_tree.fit(X_train,y_train)

#Set mlflow experiment
mlflow.set_experiment("Loan Experiment")

#Model evaluation metrics
def eval_metrics(actual,pred):
    pass


#ML logging
def mlflow_logging(model,X,y,name):
    with mlflow.start_run() as run:
        pass


mlflow_logging(model_tree,X_test,y_test,"DecisionTreeClassifier")