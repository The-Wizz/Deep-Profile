import os
import urllib.request
import urllib.parse
import urllib.error

import codecs
import requests
import json
from flask import jsonify

import face_recognition
from instagram_private_api import Client, ClientCompatPatch

import logging

log = logging.getLogger(__name__)


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def get_user_id(username):
    req = requests.get('https://www.instagram.com/{}/?__a=1'.format(username))
    user_id = req.json()['graphql']['user']['id']
    return user_id


def get_instagram(input_instagram, input_path_to_known_picture, input_firstname, input_lastname, input_email):
    settings_file = "./test_credentials.json"
    with open(settings_file) as file_data:
        cached_settings = json.load(file_data, object_hook=from_json)

    print(cached_settings['cookie'])
    return

    user_name = 'xxx'
    password = 'xxx'

    api = Client(user_name, password, settings=cached_settings)

    listofusers = api.search_users(input_instagram)
    print(listofusers)
    return listofusers
    print("# user authenticated")

    user_id = get_user_id(input_instagram)
    # user_id = api.authenticated_user_id
    print("user_id: " + user_id)
    items = api.user_feed(user_id)['items']

    print(items)

    imagesURL = []
    for count, item in enumerate(items):
        # print(item)
        image_versions2 = item['image_versions2']['candidates']
        image_url = image_versions2[0]['url']
        # print(image_url)
        imagesURL.append(image_url)

    # print("# got images")

    known_image = face_recognition.load_image_file(
        "./uploads/" + input_path_to_known_picture)
    known_faces = face_recognition.face_encodings(known_image)
    root_download_path = "./instagram-downloads/"

    counter = 0
    for url_to_image in imagesURL[:]:
        path_to_download = root_download_path + input_firstname + "-" + \
            input_lastname + "-" + input_email + str(counter) + ".jpg"
        # print(path_to_download)

        urllib.request.urlretrieve(url_to_image, path_to_download)
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
