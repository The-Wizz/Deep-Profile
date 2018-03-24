import os
from werkzeug.utils import secure_filename


def prepare_request(app, request):

    # Save the file
    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file.close

    requestData = {
        'firstname':    request.form['firstname'],
        'lastname':     request.form['lastname'],
        'email':        request.form['email'],
        'birthday':     request.form['birthday'],
        'keywords':     request.form['keywords'],
        'address':      request.form['address'],
        'instagram':    request.form['instagram'],
        'image':        filename
    }

    return requestData
