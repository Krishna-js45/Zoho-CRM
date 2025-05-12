from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample customer data
customers = [
    {"id": 1, "name": "Raj", "email": "raj@example.com"},
    {"id": 2, "name": "Aditi", "email": "aditi@example.com"}
]

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@app.route('/customer/<int:id>', methods=['GET'])
def get_customer(id):
    customer = next((c for c in customers if c["id"] == id), None)
    return jsonify(customer) if customer else ("Customer not found", 404)

@app.route('/customer', methods=['POST'])
def add_customer():
    new_customer = request.json
    new_customer["id"] = len(customers) + 1
    customers.append(new_customer)
    return jsonify(new_customer), 201

if __name__ == '__main__':
    app.run(debug=True)
