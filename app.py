from flask import Flask, render_template, request, Response, jsonify
import requests
import json.decoder
from docx import Document
from io import BytesIO
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# API base URL
API_BASE_URL = os.getenv('https://api.sampleapis.com/wines/')

# Landing page route
@app.route('/')
def landing():
    return render_template('landingpage.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

# Search page route
@app.route('/search')
def search():
    return render_template('search.html')

# Search results route
@app.route('/results')
def results():
    global returned_wines
    wine_type = request.args.get('type')
    country = request.args.get('country')
    rating = request.args.get('rating')

    # validate inputs
    valid_types = ['sparkling', 'rose', 'whites', 'reds', 'dessert', 'port']
    valid_countries = ['Argentina', 'Australia', 'Chile', 'France', 'Italy', 'Germany', 'Portugal', 'Spain', 'South Africa', 'United States']

    if wine_type not in valid_types:
        return "Invalid wine type", 400
    if country and country not in valid_countries:
        return "Invalid country", 400
    if rating and (int(rating) < 1 or int(rating) > 5):
        return "Invalid rating", 400

    # construct API URL
    api_url = f"{API_BASE_URL}{wine_type}"
    if country:
        api_url += f"?country={country}"
    if rating:
        api_url += f"&rating={rating}"
    
    # fetch data from API
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        returned_wines = response.json()
    except requests.RequestException as e:
        return f"Error fetching data from API: {e}", 400
    except json.decoder.JSONDecodeError as e:
        return f"Error decoding JSON response from API: {e}", 500 

    return render_template('results.html', wines=returned_wines, type=wine_type)

def create_document(wine):
    document_content = (
        f"Title: {wine['wine']}\n"
        f"Location: {wine['location']}\n\n"
        f"Winery: {wine['winery']}\n\n"
    )

    doc = Document()
    doc.add_paragraph(document_content)

    output = BytesIO()
    doc.save(output)
    output.seek(0)

    return Response(output.read(), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

@app.route('/download/<int:wine_id>')
def download_wine(wine_id):
    global returned_wines
    
    for wine in returned_wines:
        if wine['id'] == wine_id:
            return create_document(wine)
    
    # If wine_id is not found, return a custom error message and HTTP status code
    return "Wine not found", 404

if __name__ == '__main__':
    app.run(debug=True)

