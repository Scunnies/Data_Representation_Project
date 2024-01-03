# Data Representation Project - January 2023
#### G00411277 Eleanor Sammon
***

This project is a web application built with Flask that provides a RESTful API for managing a database of craft supplies. It includes a simple web interface to perform CRUD operations on the data.

## Files

1. **app.py:**
   - Main Flask application file.
   - Endpoints for retrieving all products, retrieving a product by ID, and serving a web page to view products.
   - Utilizes Flask, Flask-CORS, and Flask-SQLAlchemy.

2. **dbconfig.py:**
   - Configuration file containing MySQL connection details.

3. **ProductDAO.py:**
   - Data Access Object (DAO) for interacting with the MySQL database.
   - Implements CRUD operations (Create, Read, Update, Delete) for products.

4. **Productviewer.html:**
   - HTML and JavaScript for a simple web page to view, create, update, and delete products.
   - Uses jQuery for AJAX calls to interact with the Flask API.

5. **products_db.sql:**
   - MySQL script for creating the database (`products_db`) and the `products` table.
   - Inserts initial sample data into the `products` table.

## How to Run

### Install dependencies using:
   `pip install Flask Flask-CORS Flask-SQLAlchemy mysql-connector-python`

### Execute the MySQL script to create the database and table:
mysql -u <your_mysql_username> -p < products_db.sql (replacing with your own username)

### Run the Flask application in the console/terminal:
python app.py
Open your browser and go to http://localhost:5000 to view the Craft Supplies Database.

## Interactions
The Flask API (app.py) serves as the backend, providing endpoints for retrieving, creating, updating, and deleting products.
The web page (Productviewer.html) interacts with the Flask API through AJAX calls using jQuery.

## Features
CRUD functionality for managing products.
Web interface for interaction with the Craft Supplies Database.
Automatic database connection initialisation in case of failures.
Confirmation step before deleting or updating a record to prevent accidental data modifications.
