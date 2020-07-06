import os
from flask import Flask,redirect,url_for,render_template,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

from os import path 
if os.path.exists("env.py"):
     import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


@app.route("/")
def home():
    return "<h1>Hello world</h1>"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)