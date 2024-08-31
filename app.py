import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])

def predict():
    High_Temperature = float(request.form['High_Temperature'])
    Low_Temperature = float(request.form['Low_Temperature'])
    Humidity = float(request.form['Humidity'])
    Number_of_Occupants = float(request.form['Number_of_Occupants'])
    Number_of_Rooms = float(request.form['Number_of_Rooms'])
    Solar_Irradiance = float(request.form['Solar_Irradiance'])
    Battery_Storage = float(request.form['Battery_Storage'])
    HVAC_Usage_Hour = float(request.form['HVAC_Usage_Hour'])
    unit_price = float(request.form['unit_price'])
    features = np.array([[High_Temperature, Low_Temperature,Humidity,Number_of_Occupants,Number_of_Rooms,Solar_Irradiance,Battery_Storage,HVAC_Usage_Hour]])
    prediction = model.predict(features)
    price = unit_price * prediction
    return render_template("index.html", prediction_text = "Predicted Price{} Rupees and energy usage{} Kw-Hr".format(price,prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)
