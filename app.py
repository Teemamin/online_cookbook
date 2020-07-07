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

@app.route('/')
@app.route("/home")
def home():
    return render_template("index.html",recipes=mongo.db.recipe_collections.find(),owner=mongo.db.recipe_owner.find())


@app.route("/addrecipe")
def addrecipe():
    return "<h1>hello again</h1>"


@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    the_recipe = mongo.db.recipe_collections.find_one({"_id": ObjectId(recipe_id)})
    the_recipe_owner = mongo.db.recipe_owner.find()
    return render_template("get_recipe.html", recipes= the_recipe, recipe_owner = the_recipe_owner)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)