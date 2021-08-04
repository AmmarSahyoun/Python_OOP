'''Flask is a python  microframework used to build web applications and REST APIs.'''
''' Flask’s main job is to handle HTTP requests and route them to the appropriate function in the app'''
from flask import Flask, request, jsonify
app = Flask(__name__)
countries = [
     {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},   ]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/countries", methods=['GET'])
def get_countries():
    return jsonify(countries)

@app.route("/countries", methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

# cmd >>> curl 127.0.0.1:5000/countries
# curl -i 127.0.0.1:5000/countries -X POST -H 'Content-Type: application/json' -d "{"name":"Germany", "capital": "Berlin", "area": 357022}"
