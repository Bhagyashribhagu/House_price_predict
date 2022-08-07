from flask import Flask , jsonify , render_template , request
import config
from project_app.utils import house_predict

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print('Welcome to flask')
    return 'Hello flask and Hello House_predict'

@app.route('/predicted_price')
def get_predicted_price():

    Taxi_dist    = 7845
    Market_dist  = 6461
    Hospital_dist = 5785
    Carpet_area   =  1900
    Builtup_area  = 2144
    Parking_type  = open
    City_type     = 'CAT B'

    result = house_predict(Taxi_dist ,	Market_dist	,Hospital_dist ,Carpet_area	,Builtup_area,Parking_type,	City_type)
    price = result.get_predicted_price()
    return jsonify({ 'Result' : price})

if __name__ == '__main__':
    app.run()


