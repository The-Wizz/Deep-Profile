import os
from werkzeug.utils import secure_filename


def prepare_request(app, request):
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

    return requestData
