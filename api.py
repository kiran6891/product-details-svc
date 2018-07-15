from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ProductDetails(Resource):


    def get(self):
        product_details = {
            "id": "MBP1",
            "name": "MacBook Pro",
            "description": "This is an awesome MacBook Pro"
        }
        return product_details

api.add_resource(ProductDetails, "/product/MBP1/details")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)