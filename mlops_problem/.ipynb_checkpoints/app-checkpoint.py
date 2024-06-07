import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import joblib
import numpy as np
import logging
from dotenv import load_dotenv
from pathlib import Path
import re
from datetime import datetime

load_dotenv()

class Config:
    TRAIN_FILE_PATH = os.getenv('TRAIN_FILE_PATH')
    INFERENCE_FILE_PATH = os.getenv('INFERENCE_FILE_PATH')
    MODEL_FOLDER = '/models'
    timestamp = datetime.now().strftime("%Y_%m_%d")

app = FastAPI()


def get_model_path(model_folder, latest=True, specified_model=None):
    """
    Get the latest version of the model from the model folder.
    If latest is False, return the specified model path if it exists in the model folder.

    Args:
        model_folder (str): Path to the model folder.
        latest (bool): Flag to get the latest model. Default is True.
        specified_model (str): Path to the specified model. Required if latest is False.

    Returns:
        str: Path to the model file.
    """
    if latest and specified_model:
        logging.info(f"latest flag is set and specified model flag is set, returning latest model")
        
    if latest:
        model_files = os.listdir(model_folder)
        pattern = re.compile(r'sensor_data_classifier_(\d{4}_\d{2}_\d{2})\.pkl')
        
        models_with_dates = {}
        
        for model_file in model_files:
            match = pattern.search(model_file)
            if match:
                date_str = match.group(1)
                date_obj = datetime.strptime(date_str, '%Y_%m_%d')
                models_with_dates[model_file] = date_obj

        if not models_with_dates:
            raise FileNotFoundError("No valid model files found in the model folder.")

        latest_model_file = max(models_with_dates, key=models_with_dates.get)
        latest_model_path = os.path.join(model_folder, latest_model_file)
        return latest_model_path
        
    else:
        if specified_model is None:
            raise ValueError("specified_model must be provided if latest is False.")
        
        specified_model_path = os.path.join(model_folder, specified_model)
        if not os.path.exists(specified_model_path):
            raise FileNotFoundError(f"The specified model '{specified_model}' does not exist in the model folder.")
        
        return specified_model_path

#model_path = get_model_path(Config.MODEL_FOLDER)

#try:
#    model = joblib.load(model_path)
#    logging.info(f"Model loaded successfully from {model_path}")
#except Exception as e:
#    logging.error(f"Failed to load model from {model_path}: {e}")
#    raise

class SensorData(BaseModel):
    sensor_1: float
    sensor_2: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sensor Data Classifier API"}

@app.post("/predict")
def predict(data: SensorData, model: str = Query(None, description="Specify the model file name or leave empty for latest")):
    try:
        if model:
            model_path = get_model_path(Config.MODEL_FOLDER, latest=False, specified_model=model)
        else:
            model_path = get_model_path(Config.MODEL_FOLDER)
        
        loaded_model = joblib.load(model_path)
        logging.info(f"Model loaded successfully from {model_path}")

        # Extract data and prepare for prediction
        X_inference = np.array([[data.sensor_1, data.sensor_2]])
        # Run inference
        y_pred = loaded_model.predict_proba(X_inference)[:, 1]
        prediction = np.round(y_pred, 0)[0]
        return {"prediction": int(prediction)}
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

