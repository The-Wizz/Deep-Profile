import os
import urllib

from flask import jsonify

import face_recognition
from instagram_private_api import Client, ClientCompatPatch


def get_user_id(username):
    import requests
    req = requests.get('https://www.instagram.com/{}/?__a=1'.format(username))
    user_id = req.json()['graphql']['user']['id']
    return user_id


def get_instagram(input_instagram, input_path_to_known_picture, input_firstname, input_lastname, input_email):
    user_name = 'yellowrain184'
    password = 'opencodes'
    api = Client(user_name, password)

    user_id = get_user_id(input_instagram)
    items = api.user_feed(user_id)['items']

    imagesURL = []
    for count, item in enumerate(items):
        image_versions2 = item['image_versions2']['candidates']
        image_url = image_versions2[0]['url']
        imagesURL.append(image_url)

    known_image = face_recognition.load_image_file(
        "../" + input_path_to_known_picture)
    known_faces = face_recognition.face_encodings(known_image)
    root_download_path = "./instagram-downloads/"

    counter = 0
    for url_to_image in imagesURL[:]:
        path_to_download = root_download_path + input_firstname + "-" + \
            input_lastname + "-" + input_email + str(counter) + ".jpg"
        urllib.urlretrieve(url_to_image, path_to_download)
        counter += 1
        for known_face in known_faces:
            try:
                unknown_image = face_recognition.load_image_file(
                    path_to_download)
            except IOError:
                break
            unknown_faces = face_recognition.face_encodings(unknown_image)
            wasnt_found = True
            for unknown_face in unknown_faces:
                result = face_recognition.compare_faces(
                    [known_face], unknown_face)
                if True in result:
                    wasnt_found = False
            if wasnt_found:
                imagesURL.remove(url_to_image)
                os.remove(path_to_download)

    output_data = {}
    output_data["pictures"] = imagesURL
    return output_data
