from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
from dotenv import load_dotenv
import json
import logging

load_dotenv()


# def list_all_users():
#     print("lets get users")
#     # Start listing users from the beginning, 1000 at a time.
#     try:
#         page = auth.list_users()
#         while page:
#             for user in page.users:
#                 print("User: " + user.email)
#             # Get next batch of users.
#             page = page.get_next_page()
#     except Exception as e:
#         print("Error listing users: " + str(e))
#         return


# FIREBASE_SECRET = json.loads(os.getenv("LINK_REACH_SERVICE_ACCOUNT"))
# print("helelo world")
# cred = credentials.Certificate(FIREBASE_SECRET)
# wtf = firebase_admin.initialize_app(cred)
# print("wtf:", wtf)
# logging.info("Firebase Admin SDK initialized successfully.")

# list_all_users()

# Define the Firestore client
# db = firestore.client()

# Initialize the Firebase Admin SDK
# try:
#     firebase_admin.initialize_app( firebase_admin.credentials.Certificate(FIREBASE_SECRET))
#     logging.info('Firebase Admin SDK initialized successfully.')
# except Exception as e:
#     logging.error('Failed to initialize Firebase Admin SDK: %s', e)
#     raise e
