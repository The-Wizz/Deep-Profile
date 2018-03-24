import tweepy
import urllib
import face_recognition
from connection_helper import initialize_api

input_name = "Florian Rusch"
input_dob = "08.09.1995"
input_job = "student hochschule karslruhe"
# input_picture = 

api = initialize_api()

# stanford_tweets = api.user_timeline('stanford')
# for tweet in stanford_tweets:
#    print( tweet.created_at, tweet.text)

users = api.search_users(input_name)
for user in users:
    print user.name

    url = user.profile_image_url

    url = url.replace('_normal', '')

    known_image = face_recognition.load_image_file("ex_photo_known.jpg")

    urllib.urlretrieve(url, "test.jpg")
    unknown_image = face_recognition.load_image_file("test.jpg")
    
    for recognized_face_know_face in face_recognition.face_encodings(known_image):
        for recognized_face_unknown_face in face_recognition.face_encodings(unknown_image):
            result = face_recognition.compare_faces([recognized_face_know_face], recognized_face_unknown_face)
            if result:
                print result
                break
