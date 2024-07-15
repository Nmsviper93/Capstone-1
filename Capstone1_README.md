# Wine Wanderer App

The Wine Wanderer App is a Flask-based web application that allows users to search for wines based on type and rating. It integrates with an external API to fetch wine data and provides functionality to download wine details as a Word document.


## Table of Contents

### Features

### Installation

### Usage

### Testing

### Technologies Used

### Contributing

### License

-------------------------------

## Features

-**Landing Page:** Welcomes users and provides an entry point to start searching for wines.

-**Search Page:** Allows users to specify wine type (e.g., red, white) and rating.

-**Results Page:** Displays search results fetched from an external API, including wine details and an option to download wine information as a Word document.

-**Download Functionality:** Enables users to download wine details in a structured format for offline use.

-------------------------------

## Installation

To run the Wine Wanderer App locally, follow these steps:

1. **Clone the repository:**

bash
git clone https://github.com/yourusername/wine-wanderer-app.git
cd wine-wanderer-app


2. **Setup virtual environment:**

bash
python -m venv venv
source venv/bin/activate   ## On Windows use `venv\Scripts\activate`

3. **Install dependencies:**

bash
pip install -r requirements.txt


4. **Run the Flask application:**

bash
python app.py


**Access the application:**

Open a web browser and go to http://localhost:5000 to view the app.

-------------------------------

### Usage

- **Landing Page:** Upon accessing the application, users are greeted with a welcoming landing page introducing the app and providing links to start searching for wines.

- **Search Page:** Users can select a wine type (e.g., red, white) and specify a rating (1-5) to search for wines matching their criteria.

- **Results Page:** Displays a list of wines based on the search criteria, including details such as wine name, location, and average rating. Each wine entry also includes a link to download its details as a Word document.

- **Download Functionality:** Clicking on the "Download" link next to each wine on the results page allows users to download comprehensive wine details for offline reference.

-------------------------------

## Testing

To run the tests for the Wine Wanderer App, execute the following command:

bash
python -m unittest test_app.py


The tests cover unit testing of individual components (test_app.py) and integration testing of multiple components working together (test_integration.py). Ensure the Flask app (app.py) is running or deploy to a test environment before running tests.

-------------------------------

## Technologies Used

-Python: Programming language used for backend development.

-Flask: Web framework used for building the web application.

-HTML/CSS: Frontend design and styling of web pages.

-Requests: Python library used for making HTTP requests to fetch wine data from an external API.

-python-docx: Python library used for creating Word documents to download wine details.

-------------------------------

## Contributing

Contributions to the Wine Wanderer App are welcome! If you find any issues or have suggestions for improvement, please submit an issue or pull request. For major changes, please open an issue first to discuss what you would like to change.

-------------------------------

## License

MIT License