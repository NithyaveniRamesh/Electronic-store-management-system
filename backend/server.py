from flask import Flask, request, jsonify
import products_dao
import uom_dao
import json
from sql_connection import get_sql_connection
import orders_dao
app = Flask(__name__)

connection = get_sql_connection()

@app.route('/get_products', methods=['GET'])
def get_products():
     products = products_dao.get_all_products(connection)
     response = jsonify(products)
     response.headers.add('Access-Control-Allow-origin', '*')
     return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/delete_products', methods=['POST'])
def delete_products():
     return_id = products_dao.delete_products(connection, request.form['product_id'])
     response = jsonify({
        'product_id' : return_id
     })
     response.headers.add('Access-Control-Allow-origin', '*')
     return response

@app.route('/insertOrder', methods=['Post'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
     products = orders_dao.get_all_orders(connection)
     response = jsonify(products)
     response.headers.add('Access-Control-Allow-origin', '*')
     return response

@app.route('/insertProduct', methods=['Post'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response


if __name__ == '__main__':
    print("Starting python flask server for electronics store management system")
    app.run(port=5000)


