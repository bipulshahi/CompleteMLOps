from sklearn.pipeline import Pipeline
from Myloanapp.config import config
import Myloanapp.processing.preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline = Pipeline([
    ('MeanImputation' , pp.MeanImputer(variables = config.NUM_FEATURES)),
    ('ModeImputation' , pp.ModeImputer(variables = config.CAT_FEATURES)),
    ('DomainProcessing' , pp.DomainProcessing(config.FEATURES_TO_MODIFY,config.FEATURES_TO_ADD)),
    ('DropFeatures' , pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
    ('LabelEncoder' , pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
    ('LogTransform' , pp.LogTransform(variables=config.LOG_FEATURES)),
    ('MinMaxScale', MinMaxScaler()),
    ('LogisticClassifier' , LogisticRegression(random_state=0))
])