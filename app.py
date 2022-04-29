import flask
from flask import request, jsonify, Flask
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

file = open('vetcustomers.txt', 'r')
customersData = json.load(file)

'''
Customers = [
    {"id":1,
     "name": "Scarlett",
     "petName":"Jackson",
     "petType":"dog",
     "reasonForLastVisit":"Deworming"},
    {"id":2,
     "name": "Ellie",
     "petName":"Clover",
     "petType":"cat",
     "reasonForLastVisit":"Checkup"},
    {"id":3,
     "name": "Bart",
     "petName":"Santa's Little Helper",
     "petType":"dog",
     "reasonForLastVisit":"quadruplets"}
]'''

@app.route('/', methods=['GET'])
def home():
    return "<h1>We're a vets, okay.</h1>"

@app.route('/api/customers/all', methods=['GET'])
def customersAll():
    return jsonify(customersData)

@app.route('/api/customers', methods=['GET'])
def customersById():
    for item in customersData:
        if item['id'] == request.args:
            results.append(jsonify(item))
        else:
            return "No customer with that ID"
    
    results = []
  
    for Customer in customersData:
        if Customer['id'] == id:
            results.append(Customer)

    return jsonify(results)

if __name__=='__main__':
    app.run()
