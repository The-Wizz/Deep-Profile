import os
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import send_from_directory
from flask import url_for
from werkzeug.utils import secure_filename


def hello_world(app, request):
    requestData = {
        'firstname':    request.form['firstname'],
        'lastname':     request.form['lastname'],
        'email':        request.form['email'],
        'birthday':     request.form['birthday'],
        'keywords':     request.form['keywords'],
        'address':      request.form['address'],
    }

    # Save the file
    file = request.files['file']
    filename = secure_filename(requestData['firstname'] + "_" + requestData['lastname'] + "_" + requestData['email'])
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    requestData['image'] = filename


    # Do some amazing stuff here!!!
    # TODO replace requestData with your data!
    responseData = requestData

    return jsonify(responseData)
