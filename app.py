from flask import Flask, jsonify, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import send_from_directory
import os
import json
import random
from flask_cors import CORS

app = Flask(__name__, static_folder='resource')
CORS(app)

script_dir = os.path.dirname(__file__)  # Directory of the current script
abs_file_path = os.path.join(script_dir, 'mcq_data.json')

# Load data from JSON file
with open(abs_file_path, 'r') as file:
    data = json.load(file)

# Initialize Limiter with default rate limits (10 requests per minute)
limiter = Limiter(
    get_remote_address,
    app = app
)

#Check if the server is working
@app.route('/', methods=['GET'])
def checkServer():
    return make_response({'status': 'OK'})


# Define endpoint to get 10 random elements with rate limiting
@app.route('/getMCQ', methods=['GET'])
@limiter.limit("5 per 1 minutes")  # Rate limit
def random_elements():
    try:
        # Getting 10 random data from mcq_data.json file.
        random_selection = random.sample(data, 10)
        return jsonify(random_selection)
    except Exception as e:
        # Handling errors
        error_message = "An error occurred while processing the request."
        return make_response(jsonify({'error': error_message}), 500)

@app.route('/resource/<path:filename>')
def get_image(filename):
    return send_from_directory(app.static_folder, filename)

# Error handler for 404 Not Found errors
@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

# Error handler for 429 Too Many Requests errors
@app.errorhandler(429)
def rate_limit_error(error):
    return make_response(jsonify(
        {'error': 'Too Many Requests',
        'message': 'Rate limit 1 request per 10 minutes'}
        ), 429)

if __name__ == '__main__':
    app.run(debug=True)
