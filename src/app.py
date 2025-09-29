from fastapi import FastAPI

from fraud_agent import run_fraud_agent
from schema import FraudGuardResult, QueryIn

app = FastAPI(title="FraudGuard API")


@app.post("/FraudDetective", response_model=FraudGuardResult)
async def analyze(input_data: QueryIn):
    raw = run_fraud_agent(input_data.query)
    return FraudGuardResult(**raw)
