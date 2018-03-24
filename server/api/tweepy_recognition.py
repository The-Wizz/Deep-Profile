import tweepy
import urllib
import face_recognition
from flask import jsonify
from tweepy_connection_helper import initialize_api

def get_twitter(input_first_name, input_last_name, input_email, input_path_to_known_picture):

    api = initialize_api()

    users = api.search_users(input_first_name + " " + input_last_name)

    found_user = None

    for current_searching_user in users:
        print current_searching_user.name

        url = current_searching_user.profile_image_url

        url = url.replace('_normal', '')

        known_image = face_recognition.load_image_file("../" + input_path_to_known_picture)

        path_to_unkown_picture = input_first_name + "-" + input_last_name + "-" + "twitter" + ".jpg"

        urllib.urlretrieve(url, path_to_unkown_picture)
        unknown_image = face_recognition.load_image_file(path_to_unkown_picture)

        is_done = False
        for recognized_face_know_face in face_recognition.face_encodings(known_image):
            if is_done:
                break
            for recognized_face_unknown_face in face_recognition.face_encodings(unknown_image):
                result = face_recognition.compare_faces([recognized_face_know_face], recognized_face_unknown_face)
                if result:
                    print result
                    found_user = current_searching_user
                    is_done = True
                    break
    
    output_data = {}
    if found_user:
        output_data['number_of_followers'] = found_user.followers_count
        output_data['link_to_profile_picture'] = found_user.profile_image_url.replace('_normal', '')
        output_data['profile_description'] = found_user.description
        output_data['location'] = found_user.location
        output_data['creation_date'] = found_user.created_at
        output_data['linkToProfile'] = found_user.url
    return output_data
