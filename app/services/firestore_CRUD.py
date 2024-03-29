# Initialize the Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
from dotenv import load_dotenv
import json
import logging

load_dotenv()


# Initialize the Firebase Admin SDK
try:
    FIREBASE_SECRET = json.loads(os.getenv("LINK_REACH_SERVICE_ACCOUNT"))
    cred = credentials.Certificate(FIREBASE_SECRET)
    firebase_admin.initialize_app(cred)
    logging.info("Firebase Admin SDK initialized successfully.")
except Exception as e:
    logging.error("Failed to initialize Firebase Admin SDK: %s", e)
    raise e

# Define the Firestore client
db = firestore.client()


# Now you can use the Firebase Admin SDK to interact with Firebase Authentication
# For example, to list all users:
def list_all_users():
    try:
        # Start listing users from the beginning, 1000 at a time.
        page = auth.list_users()
        print("page:", page)
        while page:
            for user in page.users:
                print("User: " + user.email)
            # Get next batch of users.
            page = page.get_next_page()
    except Exception as e:
        logging.error("Error listing users: %s", e)
        raise e


def create_record(collection_name, data):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id


def create_record_with_id(collection_name, doc_id, data):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.set(data)
    print("createdwithid", doc_ref.id)
    return doc_ref.id


def read_collection(collection_name):
    col_ref = db.collection(collection_name).get()
    print(col_ref)
    collection = [
        {"id": doc.id, **doc.to_dict()} for doc in col_ref
    ]  # id must be manually included
    return collection


def find_document(collection, field, value):
    doc_ref = db.collection(collection).where(field, "==", value).get()
    document = [
        {"id": doc.id, **doc.to_dict()} for doc in doc_ref
    ]  # id must be manually included
    return document


def find_document_by_id(collection, id):
    doc = db.collection(collection).document(id).get()
    if doc.exists:
        return doc.to_dict()
    else:
        print("No such document!")
        return {}


def update_document(collection, doc_id, field, value):
    doc_ref = db.collection(collection).document(doc_id)
    doc_ref.update({field: value})
    return doc_ref.id


def delete_document_by_id(collection, doc_id):
    db.collection(collection).document(doc_id).delete()
    return doc_id


def update_link_clicks(doc_id, click_record):
    doc_ref = db.collection("links").document(doc_id)
    doc_ref.update({"clicks": firestore.ArrayUnion([click_record])})
    return doc_ref.id
