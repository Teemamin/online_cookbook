# TESTING: 
## User story Test:
* Landing page: as a user browsing for food recipes: our home page presents the user with enticing slide show of food imgaes, and scrollable
recipes with brief captivating descriptions and sample images, when a user clicks on either the image , the description link ot the view recipe 
button, it will redirect the user to a page that displays the recipe and its full instructions.
* Navigation: 
1. The search functionality: a user that doesn't have patience to scroll through our collections or a user that knows exactly what they are
looking for can easily search for our well indexed search feild, which will present the user with the search results based on their input
and in the case that the recipe they are searching for is not available: our page will display: "recipe not available" 
2. Login/logout: 
* The site interchangeably displays either login option if there is no user in session or logout option if there is a user in session: when clicked by a user it will display a login page with username input
feild,and a small note that indicates to the user to either input their username if they are already registered or click the registration link which will
redirect the user to a simple registration page for a basic authentication which checks the name inputed against the username collection in
mongodb, if the username doesn't exist: it will register the user, redirect to the home page and flash "successfully registered: Now you can add new recipes!"
and if the username already exist: it will redirect the user to the login page and flash "username already exist"
3. After the user logs in and is in session: the add recipe option in the navigation bar becomes visible and accessible to the user,
Add recipe onclick: will redirect a user to a page with form input and summernote wysiwyg API textarea feilds for recipe steps and instuction collection, all input feilds must be
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
1. if the user is logged in: Asides from being able to view the recipe instructions and steps 
the edit and delete buttons on the individual recipe page becomes visible: when either buttons are clicked : the backend flask functionality
checks to see if the person in session is the owner of the recipe and if so: access is granted, which allows the user to either edit the
recipe content or delete their recipes, else if the user attempting to make the changes is not the recipe owner: it will redirect to home page
and flash "changes can only be made by recipe owner"
2. if the user is not logged in: they can viewing our recipe collections, search recipe contents but cannot add or make any changes
* Edit and delete functionalities:
1. Edit: if a user clicks on the edit button and access is granted: the site will redirect to a page with pre populated form feilds containing
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
* I used a few different mobile devices to see the breakpoints and the way the site responds
### functionality Tests:
* manually tested all the site links to ensure they all work