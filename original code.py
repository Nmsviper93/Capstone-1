# app.py
from flask import Flask, render_template, json, request, jsonify, Response
import requests
import json.decoder

app = Flask(__name__)

# API base URL
API_BASE_URL = "https://api.sampleapis.com/wines/"

# Landing page route
@app.route('/')
def landing():
    return render_template('Capstone_landingpage.html')

# Search page route
@app.route('/Capstone_search')
def search():
    return render_template('Capstone_search.html')

# Search results route
@app.route('/Capstone_results')
def results():
    # Get search parameters from query string
    name = request.args.get('name')
    wine_type = request.args.get('type')
    country = request.args.get('country')
    rating = request.args.get('rating')

    # Construct API endpoint URL with search parameters
    api_url = f"{API_BASE_URL}{wine_type}"
    print(api_url)
    params = {}

    # include wine name as param if provided
    # if name:
    #     # modify name param to perform partial match
    #     params['name'] = f"*{name}*"
        
    # if name:
    #     params['name'] = name
    # if wine_type:
    #     params['type'] = wine_type
    # if country:
    #     params['country'] = country
    # if rating:
    #     params['rating'] = rating

    # Fetch data from API
    print(api_url)
    print(params)
    try:
        response = requests.get(api_url, params=params)
        # raise an exception for HTTP errors (4xx and 5xx)
        response.raise_for_status()
        wines = response.json()
    except requests.RequestException as e:
        return f"Error fetching data from API: {e}", 500
    except json.decoder.JSONDecodeError as e:
        return f"Error decoding JSON response from API: {e}", 500 

    return render_template('Capstone_results.html', wines=wines)

@app.route('/download/<int:wine_id>')
def download_wine(wine_id):
    # get wine data by ID from API
    api_url = f"{API_BASE_URL}/wines/{wine_id}"
    print(api_url)
    response = requests.get(api_url)
    if response.status_code == 200:
        wine = response.json()
        # generate CSV data
        csv_data = f"Name, Type, Country, Rating\n{wine['name']}, {wine['type']}, {wine['country']}, {wine['rating']}"
        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-dispostion": f"attachment; filename=wine_{wine_id}.csv"}
        )
    else:
        return "Wine not found", 404


if __name__ == '__main__':
    app.run(debug=True)

    # nick's code