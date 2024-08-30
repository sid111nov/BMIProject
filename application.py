from flask import Flask, request, render_template
from src.pipeline.CustomData import CustomData
from src.pipeline.prediction_pipeline import PredictionPipeline
import numpy as np
import os
from src.utils.logger import logger

application= Flask(__name__)

app = application

@app.route('/',methods=['GET','POST'])
def index():
    logger.info("Rendering web page")
    if (request.method=='GET'):
        
        return render_template('index.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            height=request.form.get('height'),
            weight=request.form.get('weight')           

        )
        data_df = data.get_data_as_data_frame()
        
        predict_pipeline=PredictionPipeline(data_df)
        bmi  = predict_pipeline.predict()
        bmi_result = getBMIMapping(bmi)
        logger.info(f"Bmi for input features {data_df} is {bmi_result}")



        return render_template('index.html', results=bmi_result)


def getBMIMapping(bmi):
    bmi_dict = {
        0:'Extremely Weak',1:'Weak',2:'Normal',3:'Overweight',4:'Obesity',5:'Extreme Obesity'
    }
    return bmi_dict[bmi[0]]


if __name__=="__main__":
    
    app.run(host="0.0.0.0")