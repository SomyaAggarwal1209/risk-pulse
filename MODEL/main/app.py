from fastapi import FastAPI
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib
from data_loader import load_all_data
from preprocessing import preprocess_data

app = FastAPI()

model_bank = load_model('Bank_financial_risk_model.h5')
scaler_bank = joblib.load('Bank_financial_risk_model_scaler.pkl')

model_client = load_model('Client_financial_risk_model.h5')
scaler_client = joblib.load('Client_financial_risk_model_scaler.pkl')

model_bank_intrest = load_model('Bank_Intrest_model.h5')
scaler_bank_intrest = joblib.load('Bank_Intrest_model_scaler.pkl')

model_CreditScore = load_model('CreditScore.h5')
scaler_CreditScore = joblib.load('CreditScore.pkl')
################################################################################
model_trade = load_model('Bank_financial_risk_model.h5')
scaler_trade = joblib.load('Bank_financial_risk_model_scaler.pkl')

model_scam = load_model('Bank_financial_risk_model.h5')
scaler_scam = joblib.load('Bank_financial_risk_model_scaler.pkl')
###############################################################################################################
model_repayment = load_model('Bank_financial_risk_model.h5')
scaler_repayment = joblib.load('Bank_financial_risk_model_scaler.pkl')
#################################################################################################################################
model_default = load_model('Bank_financial_risk_model.h5')
scaler_default = joblib.load('Bank_financial_risk_model_scaler.pkl')

model_market = load_model('Bank_financial_risk_model.h5')
scaler_market = joblib.load('Bank_financial_risk_model_scaler.pkl')

model_opr = load_model('Bank_financial_risk_model.h5')
scaler_opr = joblib.load('Bank_financial_risk_model_scaler.pkl')

model_var = load_model('Bank_financial_risk_model.h5')
scaler_var = joblib.load('Bank_financial_risk_model_scaler.pkl')

@app.post("/classify_risk/")
def classify_risk():
    dataframes = load_all_data()
    merged_df = preprocess_data(dataframes)

    numeric_columns = merged_df.select_dtypes(include=[np.number]).columns
    merged_df[numeric_columns] = scaler_bank.transform(merged_df[numeric_columns])

    prediction = model_bank.predict(merged_df)
    predicted_risk = (prediction > 0.5).astype(int)

    return {"predicted_risk": predicted_risk.tolist()}

@app.post("/clint_classify_risk/")
def classify_risk():
    dataframes = load_all_data()
    merged_df = preprocess_data(dataframes)

    numeric_columns = merged_df.select_dtypes(include=[np.number]).columns
    merged_df[numeric_columns] = scaler_client.transform(merged_df[numeric_columns])

    prediction = model_client.predict(merged_df)
    predicted_risk = (prediction > 0.5).astype(int)

    return {"predicted_risk": predicted_risk.tolist()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
