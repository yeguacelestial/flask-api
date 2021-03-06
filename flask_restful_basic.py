from flask import Flask, request
from flask_restful import Resource, Api


# Initializing Flask API
app = Flask(__name__)
api = Api(app)


# Handling HTTP requests of class 'Hello world'
class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello world'}

    def post(self):
        # Fetch POST request data
        some_json = request.get_json()
        return {'you sent': some_json}, 201


# Handling HTTP requests of class 'Multi'
class Multi(Resource):
    def get(self, num):
        return {'result': num*10}


# Create endpoints, and associate them with created classes
api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)
