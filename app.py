"""Python mongodb flask project"""
import os
from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    """renders home page and gets all the recipe collection from mongodb"""
    recipes = mongo.db.recipe_collections.aggregate(
        [{'$sort': {'date_created': -1}}])
    return render_template("index.html", recipes=recipes)


@app.route("/login_page")
def login_page():
    """gets the recipe owner collection from mongodb and renders the login html page"""
    username = mongo.db.recipe_owner.find()
    return render_template("login.html", user=username)


@app.route("/login", methods=["POST", "GET"])
def login():
    """gets the recipe owner collection from mongodb and checks
    if the username being submited is in the collection,if so,that
    user becomes the session user else it will redirect to regiseration page"""
    user = mongo.db.recipe_owner
    login_user = user.find_one(
        {"recipe_owner_name": request.form["recipe_owner"]})
    if login_user:
        session["user"] = request.form["recipe_owner"]
        flash("successfully logged in",'success')
        return redirect(url_for("home"))
    flash("registration required",'error')
    return redirect(url_for("register"))


@app.route("/register", methods=["POST", "GET"])
def register():
    """renders register html page,if request is post:gets the recipe
    owner collection from mogodb and checks if the name being submitted
    does not exist then it adds to the collection else if the name already
    exist,it redirects to login page"""
    if request.method == "POST":
        users = mongo.db.recipe_owner
        existing_user = users.find_one(
            {"recipe_owner_name": request.form["recipe_owner"]})
        if existing_user is None:
            users.insert(
                {"recipe_owner_name": request.form["recipe_owner"].lower()})
            session["user"] = request.form["recipe_owner"]
            flash("successfully registered",'success')
            return redirect(url_for("home"))
        flash("username already exist",'error')
        return redirect(url_for("login_page"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    """checks if there is user in session:
    if so,it removes the user from the session
    and flash logged out successfully and redirect to home page"""
    if "user" in session:
        user = session["user"]
        flash(f"you have been logged out, {user}", "success")
        session.pop("user", None)
    return redirect(url_for("home"))


@app.route("/addrecipe")
def addrecipe():
    """gets the categories collection from mongodb and renders add recipe page"""
    all_categories = mongo.db.categories.find()
    if "user" in session:
        return render_template("add_recipe.html", categories=all_categories)
    flash("login/sigup required",'error')
    return redirect(url_for("login_page"))


@app.route("/input_recipe", methods=["POST", "GET"])
def input_recipe():
    """gets the recipe collection from mongodb and if request is post
    insert the form content to the recipe collection and redirect to
    home"""
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
    flash("recipe added successfully!",'success')
    return redirect(url_for("home"))


@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    """takes the parameter from the route,gets the recipe collection from mongodb,
    and checks for the id passed in the parameter.gets the recipe owner collection
    from mongodb and renders the get recipe page lastly passes the mongo collections to be used
    in the frontend"""
    the_recipe = mongo.db.recipe_collections.find_one(
        {"_id": ObjectId(recipe_id)})
    the_recipe_owner = mongo.db.recipe_owner.find()
    return render_template("get_recipe.html", recipes=the_recipe, recipe_owner=the_recipe_owner)


@app.route("/editrecipe/<recipe_id>")
def edit_recipe(recipe_id):
    """takes the parameter passed in the route,gets the recipe collection
    from mongodb,checks if the recipe owner name matches the username in
    seesion,if so renders edit recipe page pre populated with the data.gets
    the categories collection from mongodb else it will redirect to home page
    and flash a message,that means you are not the recipe owner"""
    recipe = mongo.db.recipe_collections.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    if recipe['recipe_owner'] == session["user"]:
        return render_template("editrecipe.html", recipe=recipe, categories=categories)
    flash("changes can only be made by recipe owner",'error')
    return redirect(url_for("home"))


@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    """takes the parameter id passed in the route,gets the recipe collection
    from mongodb and updates the document accordingly and redirect to home page"""
    recipe = mongo.db.recipe_collections
    recipe.update({"_id": ObjectId(recipe_id)},
                  {'recipe_title': request.form.get('recipe_title'),
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
    return redirect(url_for("get_recipe", recipe_id=recipe_id))


@app.route("/delete_recipe/<recipe_id>", methods=["POST", "GET"])
def delete_recipe(recipe_id):
    """takes the parameter id passed in the route and checks the recipe
    collection in mongodb,if the recipe owner name in the collection is the same
    as the username in session then it will delete the data from mongodb else it
    will redirect to home page and flash a message"""
    recipes = mongo.db.recipe_collections.find_one(
        {"_id": ObjectId(recipe_id)})
    if recipes['recipe_owner'] == session["user"]:
        mongo.db.recipe_collections.remove({"_id": ObjectId(recipe_id)})
        flash("recipe deleted successfullly")
        return redirect(url_for("home"))
    flash("changes can only be done by recipe owners:",'error')
    return redirect(url_for("home"))


@app.route("/search", methods=["GET"])
def search():
    """takes in the text from the srch input form and checks the recipe
    collection in mongodb for realted data,returns the value and renders
    page"""
    search_input = request.args.get('search')
    recipes = mongo.db.recipe_collections.find({"$text": {"$search": search_input}})
    return render_template("search.html", recipes=recipes)


@app.route("/recipes/<category_name>")
def get_recipes_by_category(category_name):
    """ takes the route variable as a parameter and gets the recipe collection from mongodb:
    checks the category name against the parameter and  renders category pages accordingly"""
    recipes = mongo.db.recipe_collections.find({"category_name":category_name})
    return render_template("display_by_category.html", recipes=recipes)


@app.route("/cookware")
def cookware():
    """renders cookware page"""
    return render_template("cookware.html")


@app.route("/stats")
def stats():
    """gets recipe collection from mongodb,first it groups
    by recipe owner,count and sort and does the same process
    for category name and assigns it to a var to be used in the
    frontend.lastly it renders the stats page"""
    recipes = mongo.db.recipe_collections.aggregate([
        {"$group": {
            "_id": "$recipe_owner",
            "count": {"$sum": 1}
        }
        },
        {"$sort": {
            "_id": 1
        }}
    ])

    categories = mongo.db.recipe_collections.aggregate([
        {"$group": {
            "_id": "$category_name",
            "count": {"$sum": 1}
        }
        },
        {"$sort": {
            "_id": 1
        }}
    ])
    return render_template("stats.html", owners=recipes, category=categories)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
