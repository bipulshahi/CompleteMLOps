import os
import mlflow
import argparse
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def load_data():
    url = 'Advertising.csv'
    try:
        df = pd.read_csv(url,index_col=0)
        # fetch dataset 
        #df = fetch_ucirepo(id=186) 
        return df
    except Exception as e:
        raise e
    

def eval_function(actual,pred):
    rmse = mean_squared_error(actual,pred,squared=False)
    mae = mean_absolute_error(actual,pred)
    r2 = r2_score(actual,pred)
    return rmse,mae,r2

def main(alpha,l1_ratio):
    df = load_data()
    TARGET = "sales"
    X = df.drop(TARGET , axis = 'columns')
    y = df[TARGET]
    #X = df.data.features 
    #y = df.data.targets 
    X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8)

    mlflow.set_experiment("ML-model-1")
    with mlflow.start_run():
        mlflow.log_param("alpha",alpha)
        mlflow.log_param("l1_ratio",l1_ratio)

        model = ElasticNet(alpha = alpha, l1_ratio = l1_ratio, random_state = 6)
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)

        rmse,mae,r2 = eval_function(y_test,y_pred)

        mlflow.log_metric("RMSE",rmse)
        mlflow.log_metric("MAE",mae)
        mlflow.log_metric("R2_score",r2)
        mlflow.sklearn.log_model(model,"trained_model")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha","-a",type=float,default=0.2)
    args.add_argument("--l1_ratio","-l1",type=float,default=0.3)
    parsed_args = args.parse_args()
    #parsed_args.param1
    main(parsed_args.alpha,parsed_args.l1_ratio)