import pytest

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from Myloanapp.config import config
from Myloanapp.processing.data_handling import load_dataset
from Myloanapp.predict import generate_predictions


#output from predict script not null
#output from predict script is str data type
#the output is Y for an example data

#Fixture -> function before test function -> ensure single_prediction

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[0:1]
    result = generate_predictions(single_row)
    return result

def test_single_pred_not_none(single_prediction):       #output is not none
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction):        #data type is string
    assert isinstance(single_prediction.get('prediction')[0],str)

def test_single_pred_validate(single_prediction):
    assert single_prediction.get('prediction')[0] == 'Y'