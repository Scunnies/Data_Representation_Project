from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from ProductDAO import productDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app) # enable Cross-Origin Resource Sharing for the Flask app

try:
    # to initialise the database connection
    productDAO.initialize_database_connection()
    print("Connected to the database successfully.")
except Exception as e:
    print(f"Error connecting to the database: {e}")

# endpoint to retrieve all products
@app.route('/products')
def getAll():
    results = productDAO.getAll()
    return jsonify(results)

# endpoint to retrieve products by ID
@app.route('/products/<int:id>')
def findById(id):
    foundProduct = productDAO.findByID(id)
    return jsonify(foundProduct)

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        results = productDAO.getAll()
        return jsonify(results)
    elif request.method == 'POST':
        data = request.get_json()
        new_product_id = productDAO.create((data['name'], data['price'], data['description']))
        return jsonify({"id": new_product_id}), 201

        # Endpoint to delete a product by ID
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        # Call the delete method from the productDAO to delete the product
        productDAO.delete(id)
        return jsonify({"message": f"Product with ID {id} deleted successfully"})
    except Exception as e:
        # Handle any exceptions that may occur during deletion
        return jsonify({"error": f"Error deleting product with ID {id}: {str(e)}"}), 500
        
        # Endpoint to update a product by ID
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Call the update method from the productDAO to update the product
        productDAO.update((data['name'], data['price'], data['description'], id))
        
        return jsonify({"message": f"Product with ID {id} updated successfully"})
    except Exception as e:
        # Handle any exceptions that may occur during the update
        return jsonify({"error": f"Error updating product with ID {id}: {str(e)}"}), 500


# default route to serve the product viewer HTML file
@app.route('/')
def index():
    return app.send_static_file('productviewer.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)  # running the Flask app in debug mode with auto-reloading
    app.run(port=5000)
