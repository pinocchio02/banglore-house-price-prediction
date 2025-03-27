from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    if request.is_json:
        data = request.get_json()
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bathroom = int(data['bath'])
    else:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bathroom = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.predict_estimated_price(total_sqft, location, bhk, bathroom)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Python Flask Server Started For Home Prediction...")
    app.run(debug=True)