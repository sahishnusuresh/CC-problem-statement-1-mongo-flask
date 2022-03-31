from datetime import datetime
import pymongo


user = 'username'           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = 'password'       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = 'mongodb-service'    # service name of the mongodb admin server as set in the service for mongodb server
port = '27017'              # port number of the mongodb admin server as set in the service for mongodb server
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = pymongo.MongoClient(conn_string)
createdAt = datetime.now()

mydict = {"title": "Team Heavyweights", "author": "Sahishnu, Shreyas, sachin", "createdAt": "27-03-2022"}

db.blog.posts.insert_one({"title": "Team Heavyweights", "author": "Sahishnu, Shreyas, sachin", "createdAt": createdAt})
db.close()