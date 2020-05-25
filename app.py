from flask import Flask, request, make_response
import json
from flask_cors import CORS, cross_origin
from weather import city_weather

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
@cross_origin()
def weather():
    res = request.json
    result = res.get('queryResult')
    param = result.get('parameters')
    city = param.get('geo-city')
    w = city_weather()

    resp = w.weather_in(city)
    resp = json.dumps(resp)
    r = make_response(resp)
    r.headers['content-type'] = 'application/json'
    return r




if __name__ == '__main__':
    app.run(debug=True)