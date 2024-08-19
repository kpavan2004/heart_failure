import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from heart_failure_prediction_model.config.core import config

class DataInputSchema(BaseModel):

    age: Optional[int]
    anaemia:Optional[int] 
    creatinine_phosphokinase: Optional[int] 
    diabetes: Optional[bool]
    ejection_fraction:Optional[int] 
    high_blood_pressure:Optional[bool]
    platelets: Optional[float] 
    serum_creatinine: Optional[float]
    serum_sodium: Optional[int]
    sex: Optional[bool]
    smoking:Optional[bool]
    time: Optional[int]

class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]