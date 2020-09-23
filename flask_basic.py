from flask import Flask, jsonify, request
app = Flask(__name__)


# / Endpoint
@app.route("/", methods=['GET', 'POST'])
def index():
    # Handling a POST request
    if (request.method == 'POST'):
        # Get sent JSON, and return it
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201

    # Handling other requests
    else:
        return jsonify({"about": "Hello world!"})


# /multi/<int:num> Endpoint
@app.route('/multi/<int:num>', methods={'GET'})
def get_multiply10(num):
    return jsonify({'result': num*10})


if __name__ == '__main__':
    app.run(debug=True)
