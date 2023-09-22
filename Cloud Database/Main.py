import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def init_firestore():
    """
    Create a connection with the database
    """
    cred = credentials.Certificate("kennett-non-private-library-firebase-adminsdk-majer-bbfa3774ad.json")

    firebase_admin.initialize_app(cred, {
        "projectid" : "kennett-non-private-library"
    })

    cd = firestore.client()
    return cd

def main():
    print(init_firestore())

if __name__ == "__main__":
    main()