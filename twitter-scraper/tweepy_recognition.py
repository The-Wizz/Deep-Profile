import tweepy
import urllib
import face_recognition
from connection_helper import initialize_api

input_first_name = "Florian"
input_last_name = "Rusch"
input_email = "florian.rusch@web.de"

# input_picture = 

api = initialize_api()

# stanford_tweets = api.user_timeline('stanford')
# for tweet in stanford_tweets:
#    print( tweet.created_at, tweet.text)

users = api.search_users(input_first_name + " " + input_last_name)
for user in users:
    print user.name

    url = user.profile_image_url

    url = url.replace('_normal', '')

    known_image = face_recognition.load_image_file("ex_photo_known.jpg")

    path_to_unkown_picture = input_first_name + "-" + input_last_name + "-" + "twitter" + ".jpg"

    urllib.urlretrieve(url, path_to_unkown_picture)
    unknown_image = face_recognition.load_image_file(path_to_unkown_picture)
    
    for recognized_face_know_face in face_recognition.face_encodings(known_image):
        for recognized_face_unknown_face in face_recognition.face_encodings(unknown_image):
            result = face_recognition.compare_faces([recognized_face_know_face], recognized_face_unknown_face)
            if result:
                print result
                break
