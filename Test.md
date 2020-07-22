# TESTING: 
## User story Test:
* Landing page: as a user browsing for food recipes: our home page presents the user with enticing slide show of food imgaes, and scrollable
recipes with brief captivating descriptions and sample images, when a user clicks on either the image , the description link to the view recipe 
button, it will redirect the user to a page that displays the recipe and its full instructions.
* Navigation: 
1. The search functionality: a user that doesn't have patience to scroll through our collections or a user that knows exactly what they are
looking for can easily search for our well indexed search field, which will present the user with the search results based on their input
and in the case that the recipe they are searching for is not available: our page will display: "recipe not available" 
2. Login/logout: 
* The site interchangeably displays either login option if there is no user in session or logout option if there is a user in session: when clicked by a user it will display a login page with username input
field,and a small note that indicates to the user to either input their username if they are already registered or click the registration link which will
redirect the user to a simple registration page for a basic authentication which checks the name inputed against the username collection in
mongodb, if the username doesn't exist: it will register the user, redirect to the home page and flash "successfully registered: Now you can add new recipes!"
and if the username already exist: it will redirect the user to the login page and flash "username already exist"
3. After the user logs in and is in session: the add recipe to our collection becomes a click away,
Add recipe onclick: will redirect a user to a page with form input and summernote wysiwyg API textarea fields for recipe steps and instuction collection, all input fields must be
filled in order to successfully add a recipe.
* upon successful recipe addition: the site will redirect to the home page and flash "recipe added successfully!" and the most recent addition
shows up at the top of the collections.
4. Stats: when the stats button is clicked: it display to the user two tables :
* Table one containing the recipe contributors and the number of recipes they've added to the collection, in descending order
* Table two displays the categories and number of recipes in each category.
5. Cookware: when a user clicks on the cookware tab: it redircts to a page that showcases our recommended brand of cookwares:
* cookware purchase button onclick: when a user clicks on the purchase button, it opens a new page that takes the user to the brand manufacture's
page where purchase can be done successfully.
* Recipe onclick: when a user clicks on a recipe it can go in two directions:
1. if the user is logged in: Asides from being able to view the recipe instructions and steps, if the user in session is the recipe owner:
the edit and delete buttons on the individual recipe page becomes visible: when either buttons are clicked : the backend flask functionality
runs a check and if the user in session is the owner of the recipe: access is granted, which allows the user to either edit the
recipe content or delete their recipes.
2. if the user is not logged in: they can view our recipe collections, search recipe contents but cannot add or make any changes.
* Edit and delete functionalities:
1. Edit: if a user clicks on the edit button and access is granted: the site will redirect to a page with pre populated form fields containing
the previously added recipe data by the user making the edit after recipe is updated the site redirects back to the recipe page of the particular
recipe edited
2. Delete: if a user clicks on the delete button and access is granted: a dialogue box will pop up asking "are you sure you want to delete"
if a user click ok: recipe will be deleted and the site will redirect to the home page and flash "recipe deleted successfully!"
else if a user clicks cancel instead: it will close the dialogue box.
*Category selection:
1.  Onclick users  can easily get recipes by their categories:
* Deserts
* Main dishes
* Drinks

# Validating the HTML, CSS and JavaScript and Python:
### HTML
* Validated my HTML5 file with  [W3C validator](https://validator.w3.org) : the test did not produce HTML errors, Kindly note:
the validator highlighted jinja syntax as errors
### Python:
* Validated my python file with  [Pylint](https://www.pylint.org/#install) : the test initally produced some warnings: indicating trailing whitespace
but i have fixed it.
![python validation](/static/img/python_pylint_test.png)

### CSS :
* Validated my css file with  [W3C validator](https://jigsaw.w3.org/css-validator/validator) : the test did not produce any errors
![css validation](/static/img/cssvalidation.png)
### Javascript  :
* Validated my js file with [esprima](https://esprima.org/demo/validate.html) no errors found
![Javascript validation](/static/img/jsvalidation.png)
## Compatability Test :
### i used the following browsers the test the project:
* Google Chrome
* Mozilla Fire fox
* brave 
* Internet explorer
### Design Responsiveness:
* I tested the site on google dev tool
![google dev tool](/static/img/dev_img1.png)
(/static/img/dev_img2.png)
(/static/img/dev_img3.png)
(/static/img/dev_img4.png)

* I used a few different mobile devices to see the breakpoints and the way the site responds
### functionality Tests:
* manually tested all the site links to ensure they all work
* Python Automated test was carried out using pylint
* [return to previous doc](https://github.com/Teemamin/online_cookbook/blob/master/README.md)