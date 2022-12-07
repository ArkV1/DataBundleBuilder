import os

from google.cloud import firestore
from google.cloud.firestore_bundle import FirestoreBundle

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\Projects\Python\DataBundleBuilder/project-n1-1f74e-firebase-adminsdk-6t7o3-41f3a43480.json"

db = firestore.Client()
bundle = FirestoreBundle("quizzes")

quizzes_ref = db.collection(u'quizzes')
docs = quizzes_ref.stream()
for doc in docs:
    bundle_buffer: str = bundle.add_document(doc)

f = open("dataBundle.txt", "w")
f.write(bundle.build())
f.close()

# doc_snapshot = db.collection("quizzes").document("74WNSxi6RbYl3p378lRL").get()
# print(doc_snapshot)
# query = db.collection("quizzes")._query()
# print(query)

# # Build the bundle
# # Note how `query` is named "latest-stories-query"
# # bundle_buffer: str = bundle.add_document(doc_snapshot).add_named_query(
# #     "latest-stories-query", query,
# # ).build()

# quizzes_ref = db.collection(u'quizzes')
# docs = quizzes_ref.stream()

# for doc in docs:
#     bundle_buffer: str = bundle.add_document(doc).build()
#     # print(f'{doc.id} => {doc.to_dict()}')

# # for doc in bundle.documents:
# #     print(f'{doc.id} => {doc.to_dict()}')

# f = open("dataBundle.json", "w")
# f.write("Now the file has more content!")
# f.close()