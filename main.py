from typing import Optional
from pydantic import  BaseModel
import fastapi import FastAPI
from  Prediction.predict_premium import prediction


class Column_names(BestModel):
    age:int
    sex:str
    bmi:float
    children:int
    smoker:str
    region:str


model_name=Linear_Regression # import model file

app=FastAPI()

#Predict Route
@app.post("/prediction/")
async  def create_item(data:Column_names):

    # initializing prediction class

    pred=prediction(model_name,data)

    premium_cost=pred.prediction()
    return  premium_cost

