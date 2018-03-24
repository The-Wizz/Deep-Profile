"""
    Golden Profile
"""
from flask import Flask
from flask import request
from flask import send_from_directory
from werkzeug.utils import secure_filename
from util import prepare_request

from api.hello import hello_world


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'



# Example
# TODO remove this
@app.route('/api/hello', methods=['POST'])
def hello():
    return hello_world(prepare_request(app, request))



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
