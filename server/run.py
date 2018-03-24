"""
    Golden Profile
"""
from flask import Flask
from flask import request
from flask import send_from_directory
from werkzeug.utils import secure_filename
from util import prepare_request
from flask import jsonify

from api.hello import hello_world
from api.tweepy_recognition import get_twitter


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'



# Example
# TODO remove this
@app.route('/api/hello', methods=['POST'])
def hello():
    return hello_world(prepare_request(app, request))

# Example
# TODO remove this
@app.route('/api/twitter', methods=['POST'])
def get_twitter_data():
    input_data = prepare_request(app, request)
    output_data = get_twitter(input_data['firstname'], input_data['lastname'], input_data['email'], input_data['image'])
    return jsonify(output_data)

# For show uploaded pictures
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# For show webpage
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


# Initiate flask
if __name__ == '__main__':
    app.run(debug=True)
