from fastapi import FastAPI, Query
from typing import Optional
import utils as bazi
from fastapi import FastAPI
# from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Bazi Calculator API with /api prefix")

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # This allows all HTTP methods
    allow_headers=["*"],  # This allows all headers
)


@app.get("/api/calculate_bazi")
def calculate_bazi(
    date_input: str = Query(..., description="Birth date in YYYY-MM-DD format"),
    time_input: Optional[str] = Query(None, description="Birth time in HH:MM format (optional)"),
    sex: str = Query(..., description="Sex (male or female)")
):
    result = bazi.Api1FourPillarLuckPillar(date_input, time_input, sex)
    return {"result": result}


@app.get("/api/api2_current_energy")
def current_year_month_energy():
    result = bazi.Api2CurrentYearMonthEnergy()
    return {"result": result}


@app.get("/api/api3_five_year_forecast")
def five_year_energy_forecast():
    result = bazi.Api3FiveYearEnergyForecast()
    return {"result": result}


@app.get("/api/api4_next_week_energy")
def next_week_energy():
    result = bazi.Api4NextWeekDailyEnergy()
    return {"result": result}


@app.get("/api/api5_star_predict")
def star_predict(
        birth_date: str = Query(..., description="Birth date in YYYY-MM-DD format"),
        target_date: str = Query(..., description="Target date in YYYY-MM-DD format")
    ):
    result = bazi.Api5StarPredict(birth_date, target_date)
    return {"result": result}


@app.get("/api/api6_get_detail_date")
def get_detail_date(
        input_date: str = Query(..., description="Birth date in YYYY-MM-DD format")
    ):
    result = bazi.Api6GetDetailDate(input_date)
    return {"result": result}


