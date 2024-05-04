from flask import Flask, jsonify, request 
from pymongo import MongoClient
from flask_cors import CORS
from model.response  import get_ml_response


app = Flask(__name__)
CORS(app, origins='*')

# DATABASE_URL="mongodb+srv://SidBudhia:Sid2135@cluster1.6dallrp.mongodb.net/FYP?retryWrites=true&w=majority"
# client = MongoClient(DATABASE_URL)

client = MongoClient('mongodb://localhost:27017/')
db = client['FYP']
collection = db['abs_carbonfibre']


# res= get_ml_response(0.2, 45, 90)
# print("test", res)

@app.route("/", methods=['GET'])
def hello_server():
    return "Hello, Server!"

@app.route("/predict", methods=['GET', 'POST'])
def home():
    data = request.json

    existing_data = collection.find_one({'infill_density': data['num1'], 'raster_angle': data['num2'], 'layer_thickness': data['num3']})
    if existing_data:
        output = existing_data['result']
    
    else:
        # Call your ML model to make predictions
        # input_data = [data['num1'], data['num2'], data['num3']]
        output = get_ml_response(data['num1'], data['num2'], data['num3'])
        print("ml_output", output)
        # Save the input and output to the database for future use
        collection.insert_one({'infill_density': data['num1'], 'raster_angle': data['num2'], 'layer_thickness': data['num3'], 'result': output})

    return jsonify({'result': output})
 


# Members API route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)