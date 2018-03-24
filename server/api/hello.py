from flask import jsonify


def hello_world(requestData):
    # Do some amazing stuff here!!!
    # TODO replace requestData with your data!
    responseData = requestData

    return jsonify(responseData)
