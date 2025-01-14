import os
from pathlib import Path

from google.cloud import firestore as FirebaseFirestore, storage as FirebaseStorage
from google.cloud.firestore_bundle import FirestoreBundle

# Set the path to the credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/ark/Sync/Google Play Documents/quizatory-firebase-adminsdk-g8qqa-b9dc1169cc.json"

# Firebase Firestore data bundle builder
db = FirebaseFirestore.Client(project="quizatory")
bundle = FirestoreBundle("quizzes")
quizzes_ref = db.collection("quizzes")
docs = quizzes_ref.stream()

for doc in docs:
    bundle.add_document(doc)

# Adjust data bundle file name and path here | directory should exist already
localPath = Path.cwd()
path = localPath.joinpath('data_bundle', 'data_bundle.txt')
path.parent.mkdir(exist_ok=True, parents=True)

with open(path, "w+") as f:
    f.write(bundle.build())

# Firebase Storage directory downloader
# Download directory
path = Path('/Users/ark/Development/Projects/Python/DataBundleBuilder/')

storage_client = FirebaseStorage.Client()
bucket = storage_client.bucket('quizatory.appspot.com')
blobs_specific = list(bucket.list_blobs(prefix='images/quizzes/'))

# Downloads in to the current folder
localPath = Path.cwd()
for blob in blobs_specific:
    print(blob.name)
    filePath = blob.name.split('/', 2)[2]
    path = localPath.joinpath('data_bundle/images/quizzes/', filePath)
    path.parent.mkdir(exist_ok=True, parents=True)
    blob.download_to_filename(path)
