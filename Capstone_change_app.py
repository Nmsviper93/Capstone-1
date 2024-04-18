# app.py
from flask import Flask, render_template, json, request, send_file, Response
import requests
import json.decoder
from docx import Document
from io import BytesIO

app = Flask(__name__)

# API base URL
API_BASE_URL = "https://api.sampleapis.com/wines/" #You had the endpoint wrong
returned_wines = []

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

    global returned_wines  # Use global variable
    # Get search parameters from query string
    wine_type = request.args.get('type')

    # Construct API endpoint URL with search parameters
    api_url = f"{API_BASE_URL}{wine_type}"
    
    # Fetch data from API
    try:
        response = requests.get(api_url)
        # raise an exception for HTTP errors (4xx and 5xx)
        response.raise_for_status()
        returned_wines = response.json()

    except requests.RequestException as e:
        return f"Error fetching data from API: {e}", 400
    except json.decoder.JSONDecodeError as e:
        return f"Error decoding JSON response from API: {e}", 500 

    return render_template('Capstone_results.html', wines=returned_wines, type=wine_type)


# to create a document from the wine data
def create_document(wine):

    # Example: Extract relevant information
    document_content = ""

    document_content += f"Title: {wine['wine']}\n"
    document_content += f"Location: {wine['location']}\n\n"
    document_content += f"Winery: {wine['winery']}\n\n"

    # Create a Word document
    doc = Document()
    doc.add_paragraph(document_content)

    # Save the document to a bytesIO object
    output = BytesIO()
    doc.save(output)
    output.seek(0)

    # Return the document as a response
    return Response(output.read(), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

@app.route('/download/<string:wine_name>')
def download_wine(wine_name):
    global returned_wines  # Use global variable
    for wine in returned_wines:
        if wine['wine'] == wine_name:
            return create_document(wine)


if __name__ == '__main__':
    app.run(debug=True)
