# Data Bundle Builder from Firebase Firestore

<<<<<<< HEAD
# REQUIREMENTS
Do not forget to install Firebase CLI | otherwise you will experience authentication problems with no error messages
Other such errors might be caused by wront time set on your machine
=======
Build data bundle from Firestore documents for offline use or for data delivery via CDN
>>>>>>> 3e94e8553b164e5a43f89cdec1cd3bdf1ddd54e5

- [ ] Create CLI wrapper

## Requirements
Do not forget to install Firebase CLI
> you will experience authentication problems with no error messages if it isnt installed

### Notes

Removing sensitive data from a repository
```
$ git clone --mirror https://github.com/ArkV1/DataBundleBuilder.git
$ java -jar C:\tools\bfg-1.14.0.jar --delete-files project-n1-1f74e-firebase-adminsdk-6t7o3-41f3a43480.json DataBundleBuilder.git
$ git push --force
```

### Python Cheat sheet

Create virtual environment and activate it
```
$ python -m venv .env 
$ .\.env\Scripts\activate   
```

Install from requirements.txt 
```
$ pip install -r requirements.txt
```

Create requirements.txt 
```
$ pip freeze > requirements.txt
```

Packages update on windows: 
```
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```