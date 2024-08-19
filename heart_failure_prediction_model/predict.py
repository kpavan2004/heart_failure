import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import Union
import pandas as pd
import numpy as np

from heart_failure_prediction_model import __version__ as _version
from heart_failure_prediction_model.config.core import config
from heart_failure_prediction_model.pipeline import heart_failure_pipe
from heart_failure_prediction_model.processing.data_manager import load_pipeline


pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
heart_failure_pipe= load_pipeline(file_name=pipeline_file_name)


def make_prediction(*,input_data:Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model """
    predictions = heart_failure_pipe.predict(pd.DataFrame(input_data))
    results = {"predictions": predictions,"version": _version, "errors": None}
    print(results)

    return results

if __name__ == "__main__":

    data_in={'age':[75],'anaemia':[0],'creatinine_phosphokinase':582,'diabetes':0,
                'ejection_fraction':[20],'high_blood_pressure':[1],'platelets':265000,'serum_creatinine':1.69,'serum_sodium':130,'sex':1,'smoking':1,'time':4}
    
    make_prediction(input_data=data_in)
