import pyrebase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 600)

firebaseConfig = {
    'apiKey': "AIzaSyDF5SAD9euJbbsUEz3yQY6W3LgvA-0bM8U",
    'authDomain': "finalproject-8b6b4.firebaseapp.com",
    'projectId': "finalproject-8b6b4",
    'databaseURL': "https://finalproject-8b6b4-default-rtdb.firebaseio.com",
    'storageBucket': "finalproject-8b6b4.appspot.com",
    'messagingSenderId': "29231288442",
    'appId': "1:29231288442:web:03f8123760578266e2abc3",
    'measurementId': "G-SR5YY8FEGW"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

class signUp(MDApp):
    def build(self):
        return Builder.load_file('signup.kv')

    def create_account(self, email, password):
        emailpy = email
        passwordpy = password
        auth.create_user_with_email_and_password(emailpy, passwordpy)


if __name__ == "__main__":
    signUp().run()
