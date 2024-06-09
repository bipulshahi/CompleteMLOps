

##Virtual Environment

Install virtualenv
'''
python3 -m pip install virtualenv
'''


Check version
'''
virutalenv --version
'''

Create virtual environment
'''
virtualenv ml_package
'''

Activate Virtual environment
for linux/mac
'''
source ml_package/bin/activate
'''

for windows
'''
ml_package/Scripts/activate
'''

# Build the Package
1. Go to project directory and install dependencies
'pip install -r requirements.txt'

2. Creare pickle file after training
'python Myloanapp/training_pipeline.py'

3. Create source distribution and wheel
'python setup.py sdist bdist_wheel'


# Installation of Package

# Go to Project directory where 'setup.py' file is located

# Install Myloanapp
'source ml_package/bin/activate'
'cd Desktop'
'mkdir test-package'
'cd test-package'
'pip3 install git+https://github.com/bipulshahi/gitmlops.git'

# Enable python scriptinhg
'python3'
'import Myloanapp'
'from Myloanapp import training_pipeline'
'training_pipeline.perform_training()'

# Making Predictions on a data file
'import pandas as pd'
'test_data = pd.read_csv('/Users/bipulkumar/Desktop/test-package/test_loan.csv')'
'from Myloanapp import predict'
'predict.generate_predictions(test_data[:1])'