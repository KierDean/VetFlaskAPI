import flask  
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our program.  In the real world we would want this to be made or come from another source such as a database
PetOwners = [
    {'id': 0,
     'name': 'Keiran',
     'pet_name': 'Seal hunter',
     'pet_type': 'Otter',
     'last_visit_was_for': 'Castration'},
    {'id': 1,
     'name': 'Ahmed',
     'pet_name': 'Mac',
     'pet_type': 'Tortoise',
     'last_visit_was_for': 'Being slow even for a tortoise'},
    {'id': 2,
     'name': 'Gareth',
     'pet_name': 'Captain Jazzy Pants',
     'pet_type': 'Cat',
     'last_visit_was_for': 'Dog bite'}
]


@app.route('/', methods=['GET'])    #tell which HTTP method we are using (GET) and what route (extra bit of the URL) this method will be activated on.  In this case nothing and so home
def home():
    return "<h1>Welcome to Gareth's virtual lesson</h1><p>Sorry I am still ill.</p>" #what the api returns


# A route to return all of the available entries in our collection of pet owners.
@app.route('/api/somearea/vetcustomers/all', methods=['GET'])
def api_all():
    return jsonify(PetOwners)

@app.route('/api/somearea/vetcustomers', methods=['GET'])
def get_owner_by_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: You are an idiot."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for PetOwner in PetOwners:
        if PetOwner['id'] == id:
            results.append(PetOwner)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
