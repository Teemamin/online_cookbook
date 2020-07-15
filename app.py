import os
from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import json

from os import path
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


@app.route('/')
@app.route("/home")
def home():
    return render_template("index.html", recipes=mongo.db.recipe_collections.find())


@app.route("/login_page")
def login_page():
    username = mongo.db.recipe_owner.find()
    return render_template("login.html", user=username)


@app.route("/login", methods=["POST", "GET"])
def login():
    user = mongo.db.recipe_owner
    login_user = user.find_one(
        {"recipe_owner_name": request.form["recipe_owner"]})
    if login_user:
        session["user"] = request.form["recipe_owner"]
        return redirect(url_for("addrecipe"))
    flash("registration required")
    return redirect(url_for("register"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.recipe_owner
        existing_user = users.find_one(
            {"recipe_owner_name": request.form["recipe_owner"]})
        if existing_user is None:
            users.insert({"recipe_owner_name": request.form["recipe_owner"]})
            session["user"] = request.form["recipe_owner"]
            return redirect(url_for("home"))
        flash("username already exist")
        return redirect(url_for("login_page"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"you have been loggedout, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login_page"))


@app.route("/addrecipe")
def addrecipe():
    all_categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=all_categories)


@app.route("/input_recipe", methods=["POST", "GET"])
def input_recipe():
    recipe = mongo.db.recipe_collections
    if request.method == 'POST':
        recipe.insert({
            'recipe_title': request.form.get('recipe_title'),
            'category_name': request.form.get('category_name'),
            'prep_time': request.form.get('prep_time'),
            'cook_time': request.form.get('cook_time'),
            'servings': request.form.get('servings'),
            'recipe_owner': session["user"],
            'description': request.form.get('description'),
            'ingredients': request.form.get('ingredients'),
            'steps': request.form.get('steps'),
            'recipe_image': request.form.get('recipe_image'),
            'date_created': datetime.now()
        })

    return redirect(url_for("home"))


@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    the_recipe = mongo.db.recipe_collections.find_one(
        {"_id": ObjectId(recipe_id)})
    the_recipe_owner = mongo.db.recipe_owner.find()
    return render_template("get_recipe.html", recipes=the_recipe, recipe_owner=the_recipe_owner)


@app.route("/editrecipe/<recipe_id>")
def edit_recipe(recipe_id):
    recipe = mongo.db.recipe_collections.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    if recipe['recipe_owner'] == session["user"]:
        return render_template("editrecipe.html", recipe=recipe, categories=categories)
    else:
        flash("changes can only be made by recipe owner")
        return redirect(url_for("home"))


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe_collections
    recipe.update({"_id": ObjectId(recipe_id)},
                  {'recipe_title': request.form.get('recipe_title'),
                   'category_name': request.form.get('category_name'),
                   'recipe_owner': session["user"],
                   'description': request.form.get('description'),
                   'ingredients': request.form.get('ingredients'),
                   'steps': request.form.get('steps'),
                   'recipe_image': request.form.get('recipe_image'),
                   'date_created': datetime.now()
                   })
    return redirect(url_for("home"))


@app.route("/delete_recipe/<recipe_id>", methods=["POST", "GET"])
def delete_recipe(recipe_id):
    recipes = mongo.db.recipe_collections.find_one(
        {"_id": ObjectId(recipe_id)})
    if recipes['recipe_owner'] == session["user"]:
        mongo.db.recipe_collections.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for("home"))


@app.route("/search", methods=["GET"])
def search():
    search = request.args.get('search')
    recipes = mongo.db.recipe_collections.find({"$text": {"$search": search}})
    #if recipes.count():
    return render_template("search.html", recipes=recipes)
    #else:
        #return redirect(url_for("home"))


@app.route("/desert")
def desert():
    recipes = mongo.db.recipe_collections.find()
    return render_template("desert.html", recipes=recipes)


@app.route("/main_dishes")
def main_dishes():
    recipes = mongo.db.recipe_collections.find()
    return render_template("main_dishes.html", recipes=recipes)


@app.route("/drinks")
def drinks():
    recipes = mongo.db.recipe_collections.find()
    return render_template("drinks.html", recipes=recipes)


@app.route("/cookware")
def cookware():
    return render_template("cookware.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
