import os

from google.cloud import firestore
from google.cloud.firestore_bundle import FirestoreBundle

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\Projects\Python\DataBundleBuilder\project-n1-1f74e-firebase-adminsdk-6t7o3-b800aaa84e.json"

db = firestore.Client()
bundle = FirestoreBundle("quizzes")

quizzes_ref = db.collection(u'quizzes')
docs = quizzes_ref.stream()
for doc in docs:
    bundle_buffer: str = bundle.add_document(doc)

f = open("data_bundle.txt", "w")
f.write(bundle.build())
f.close()