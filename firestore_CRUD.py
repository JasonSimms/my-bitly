# Initialize the Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./fireBase_credentials.json")
firebase_admin.initialize_app(cred)

# Define the Firestore client
db = firestore.client()


def create_record(collection_name, data):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id


def create_record_with_id(collection_name, doc_id, data):
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.set(data)
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


def update_document(collection, doc_id, field, value):
    doc_ref = db.collection(collection).document(doc_id)
    doc_ref.update({field: value})
    return doc_ref.id


def delete_document(collection, doc_id):
    db.collection(collection).document(doc_id).delete()
    return doc_id
