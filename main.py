import os

from pathlib import Path, WindowsPath

from google.cloud import firestore as FirebaseFirestore, storage as FirebaseStorage
from google.cloud.firestore_bundle import FirestoreBundle

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\Projects\Python\DataBundleBuilder\quizatory-firebase-adminsdk-g8qqa-b9dc1169cc.json"

# Firebase Firestore data bundle builder

db = FirebaseFirestore.Client(project="quizatory")
# Bundle's collection name (should match the one in the Firestore)
bundle = FirestoreBundle("quizzes")
# Firestore collection name  (shoud match the one in the data bundle)


quizzes_ref = db.collection("quizzes")
docs = quizzes_ref.stream()
for doc in docs:
    bundle_buffer: str = bundle.add_document(doc)
# Adjust data bundle file name and path here | directory should exist already
localPath = Path.cwd()
path = localPath.joinpath('data_bundle', 'data_bundle.txt')
path.parent.mkdir(exist_ok=True, parents=True)
f = open(path, "w+")
f.write(bundle.build())
f.close()

# Firebase Storage directory downloader

# Download directory
path = WindowsPath('C:/Projects/Python/DataBundleBuilder/')

storage_client = FirebaseStorage.Client()
# Bucket name
bucket = storage_client.bucket('quizatory.appspot.com')
# List all files in the bucket
blobs = bucket.list_blobs()
# Filter files per directory (Choose directory to download from)
blobs_specific = list(bucket.list_blobs(prefix='images/quizzes/'))

# Downloads in to the current folder
localPath = Path.cwd()
for blob in blobs_specific:
    print(blob.name)
    # Need to be adjusted to your directory structure
    filePath = blob.name.split('/', 2)[2]
    # Debug correct adjustments per your needs
    # print(filePath)
    # for current folder subdirectory path adjust here
    path = localPath.joinpath('data_bundle/images/quizzes/',filePath)
    path.parent.mkdir(exist_ok=True, parents=True)
    blob.download_to_filename(path)
