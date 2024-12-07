from flask import Flask, request, jsonify
from flask_cors import CORS
import products_dov
import connection

app = Flask(__name__)
CORS(app)
connect = connection.connection()

@app.route('/addProducts', methods = ['POST'])
def add_product():
    data = {
        "product_name" : request.json.get('product_name'),
        "unit" : request.json.get('unit'),
        "price" : request.json.get('price'),
    }
    products_dov.add_products(connect, data)
    get_products()
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    data = {
        "product_id" : request.json.get('product_id'),
    }
    products_dov.delete_product(connect, data)
    get_products()
    return jsonify({"message" : "Product deleted successfully"}), 201

@app.route('/getUnit', methods = ['GET'])
def get_units():
    units = products_dov.display_units(connect)
    response = jsonify(units)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/getProducts', methods = ['GET'])
def get_products():
    products = products_dov.display_products(connect)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(port = 5000)