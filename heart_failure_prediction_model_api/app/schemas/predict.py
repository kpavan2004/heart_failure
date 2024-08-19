from typing import Any, List, Optional

from pydantic import BaseModel
from heart_failure_prediction_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    # predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "age": 75,
                        "anaemia": 0,
                        "creatinine_phosphokinase": 582,
                        "diabetes": 0,
                        "ejection_fraction": 20,
                        "high_blood_pressure": 1,
                        "platelets": 265000,
                        "serum_creatinine": 1.69,
                        "serum_sodium": 130,
                        "sex": 1,
                        "smoking": 1,
                        "time": 4,
                    }
                ]
            }
        }
