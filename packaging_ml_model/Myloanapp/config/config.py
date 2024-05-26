import pathlib
import os
import Myloanapp

PACKAGE_ROOT = pathlib.Path(Myloanapp.__file__).resolve().parent

#print(PACKAGE_ROOT)

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

TRAIN_FILE = 'train_loan.csv'
TEST_FILE = 'test_loan.csv'

MODEL_NAME = "classification.pkl"
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_models")

TARGET = 'Loan_Status'

FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 
            'Self_Employed','ApplicantIncome', 
            'CoapplicantIncome', 'LoanAmount','Loan_Amount_Term', 
            'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome','LoanAmount','Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 
                'Education', 'Self_Employed', 'Credit_History', 
                'Property_Area']

#here it is same as categorical features
FEATURES_TOENCODE = ['Gender', 'Married', 'Dependents', 
                'Education', 'Self_Employed', 'Credit_History', 
                'Property_Area']

FEATURES_TO_MODIFY = 'ApplicantIncome'
FEATURES_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome','LoanAmount']


      