ML flow is an open source platform designed to manage end-to-end machine learning lifecycle
It offers tools for experimen tracking, model management, and deployment

# Components of MLflow
1. MLflow tarcking - Record and query experiments: code, data , config and results
2. MLflow Projects - Package data science code in a format to reproduce runs on any playform
3. MLflow models - Deploy machine learning models in diverse serving environments
4. Model regitry - Store, Annotate, discover, and manage models in a central repository

# create a virtual environment
'virtualenv mlflow-env'

# activate virtual environmet
'source mlflow-env/bin/sctivate'

for windows - 'mlfow-env\Scripts\activate'

# install mlfow
'pip3 install mlflow'

# verify istallation
'mlflow'
'mlflow --version'

# start mlflow ui
mlflow ui

# 'mlflow.set_tracking_uri()' 
    connects to a tracking URI, We can also set the MLFLOW_TRACKING_URI environment variable to have MLflow find a URI from there.
    In boh cases the URI can either be a HTTP/HTTPs URI for a remore server, a database connection string, or a local path to log data to a directory. The URI defaults to mlrums.

# 'mlflow.get_tracking_uri()'

# 'mlflow.create_experiment()'

# 'mlflow.set_experiments()'

# 'mlflow.start_run()'

# 'mlflow.end_run()'

# 'mlflow.log_param()'

# 'mlflow.log_metric()'

# 'mlflow.set_tag()'

# 'mlflow.log_artifact()'

# 'mlflow.log_artifacts()'