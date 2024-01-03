# server1.py

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from ProductDAO import productDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

try:
    # Attempt to initialize the database connection
    productDAO.initialize_database_connection()
    print("Connected to the database successfully.")
except Exception as e:
    print(f"Error connecting to the database: {e}")

@app.route('/products')
def getAll():
    results = productDAO.getAll()
    return jsonify(results)

@app.route('/products/<int:id>')
def findById(id):
    foundProduct = productDAO.findByID(id)
    return jsonify(foundProduct)

@app.route('/')
def index():
    return app.send_static_file('productviewer.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    app.run(port=5000)
