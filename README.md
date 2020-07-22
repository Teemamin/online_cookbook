# Susu's online_cookbook
susu's online cookbook is a fictional site that is aimed at encouraging people to cook at home, 
and  making the process of feeding your family and loved ones less intimidating and more enjoyable.

## UX
This project gives its users the flexibilty to share their own recipes, edit, delete them

if need be and also grants them access to other users recipes and process to make cooking easy, fun and accessible to everyone

with no prior experience necessary. The site provides several ways to access its recipe Contents, shows statistics on 

recipe contributors, content category whilst also providing its users with easy access to our suggested, tried and tested cookware brands
### User Stories :
The user stories below inspired my design for the project :
#### Project owner:
* Being the project owner and the person that will love to see it succeed the most: I would like to attract users and increase our following
in hopes of creating a community for foodies, where people come to share their love for food, share family recipes, cooking tips whilst
also promoting my recommended cookware and future possiblilities of food blog & hard copy cookbooks.
#### First Time user:
* user : a user with no prior experience cooking: our step by step recipe collections and yummy food images takes the user through the journey 
of making their personalized dish experience.
* user : a user that has some experience cooking but isn't sure what they are looking for: our enticing category collections and search
option helps make does descions alot easier.
* user : the ability to share your own recipes with the community: as a user more especially if you love food like i do, will
surely be a return user given the ability to share your craft with others using our add recipe section.
#### Return users:
* user: i am a mum that loves to cook for my family: i have tired the recipes and my family loved every bit of it, so i will love to 
share my own recipes with the community to help others share that love.
* user: on my first visit to the site i had little to no prior experience with cooking but after trying the step by step recipes: i am back
for more.
* user: food blogger: i am a food blogger: with passion for sharing my craft and experience with the world, this platform is an additional
avenue of expanding my audience.
#### Wireframes: 
* To view Wireframes doc [click me](https://github.com/Teemamin/online_cookbook/tree/9c3c2b6cdfac5a91f097473a4b9e76e3a9d8dca0/wireframes).


## Features

### Existing Features

#### Create Recipe :
This feature allows users to add and share their recipe contents with other users, it requires a quick and easy username signup.
#### Read :
A user can browse the site contents and get it's recipes and process.
#### Update Recipe :
The edit feature allows the recipe owner to make changes to their contents and update the changes. Changes can only be done by recipe owner,
Note: edit button is only visible to the user that contributed the recipe
#### Delete:
The delete function allows recipe owners to delete their contents, it asks for user confirmation before deleting the data,
Note: delete button is only visible to the user that contributed the recipe
#### Statistics :
The site provides a statistics table which displays contents contributors, number of recipes contributed and a category table which displays 
recipe contents quantity based on its category.
#### Search :
The site has a search functionality that allows its users to easliy search for contents based on their names, ingredients or keywords.
#### login/logout and signup :
THe site provides a login/logout option page interchangeably for returning users and a register page for new users.
#### Cookware Brand :
The site provides easy access to our trusted brands of cookware.
#### Contact:
There is a provision for contacting us regarding any complaints or suggestions.

### Features Left to Implement
In the future release ideas:
1. A proper authentication system
2. Create personalized user page
3. Put a system in place that will allow users to connect to each other like social media 
4. User chat system 
5. Allow comments,review and ratings on recipe posts
6. Allow users to share their tested recipe pictures and experiences to create a supporting community for foodies 
7. Blog and newsletter.

## Technologies Used
### Languages, libraries, frameworks, editors and version control
* HTML5 was used to put the page structure in place [HTML](https://validator.w3.org/).
* CSS was used to style and allign images and other structures on the page  [CSS](https://www.w3.org/Style/CSS/Overview.en.html).
* Javascript was used for interactivity  [Javascript](https://www.ecma-international.org/).
* Python3 was used for the application scripting  [Python](https://www.python.org/).
* Jinja was used for the frontend templating  [Jinja](https://jinja.palletsprojects.com/en/2.11.x/).
* Mongodb was used as the application database  [mongodb](https://www.mongodb.com/).
* Heroku for hosting the application  [heroku](https://dashboard.heroku.com/).
* Summernote API was used as part of the form text area feilds to collect user inputs [summernote](https://summernote.org/).
* Bootstrap was used for page layout [bootstrap](https://getbootstrap.com/).
* Start bootstrap theme was used for the homepage [start bootstrap](https://startbootstrap.com/templates/shop-homepage/).
* Google fonts was used for the site fonts [google fonts](https://fonts.google.com/).
* Fontawesome was used for its icons  [font awesome](https://fontawesome.com/).
* Ian Lunn CSS Hover cdn was used for the site navigations  [ian lunn](https://ianlunn.github.io/Hover/).
* I used gitpod's development environment to write my code for the project  [Gitpod](https://www.gitpod.io/).
* I used github for its repo and version control of the project  [Github](https://github.com/).
 
## Testing
 * To view Test doc [click me](https://github.com/Teemamin/online_cookbook/blob/master/Test.md).
## Deployment
* Project Deployment:
#### Deploying to Heroku:
* Creating heroku app and linking to github repo:
1. On Heroku website [click here](https://dashboard.heroku.com/) I logged into my heroku dashboard :
2. Clicked on create new app: gave the app a name and chose a region
3. in my gitpod work environment CLI: $ heroku login : to login to heroku from my terminal
4. Linking Heroku to my github local repo: heroku dashboard ->settings->heroku git url (copied)
5. Gipod terminal: git remote add "the heroku git url copied from heroku site"
6. Gipod terminal: git push -u heroku master
* Creating requirements.txt: 
1. Gitpod terminal: pip3 freeze --local > requirements.txt: which installed all the necessary dependencies for the project
* Creating Procfile: 
1. Gitpod terminal: echo web: python app.py >Procfile 
* git add Procfile
* git add requirements.txt
* git commit -m "Procfile and requirements.txt added"
* git push 
* Gitpod terminal : heroku ps:scale web=1 : to start one running dyno in heroku.
* on my heroku dashboard -> settings -> revel config vars -> : i set my IP address, PORT and flask configuration variables
* lastly heroku dashboard -> open app. 
The above steps allowed me to link my flask python project from gitpod/github to heroku for hosting which enables me with a link to share
my project with others.
### Project Cloning :
Should anyone be intrested in making future enhancements to this project, you can clone the as follows:
* At the top of my repo : click on the "code" button, which will present you with the following options :
1. Clone with HTTPS or an SSH key: [Generating a new key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
* SSH key: click use SSH key : don't have any public SSH keys in your GitHub account, You can add a new public key,by clicking on the github provided link or try cloning this repository via HTTPS
* HTTPS : click on the copy icon on the right, which will copy the link on your clipbord
2. Open your Terminal : ensure that your current working directory is the location you want the clone directory to be in
3. git clone : paste in the HTTPS url you copied
4. for further info on github cloning : [Github](https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository).

## Credits
* Got some of my inspiration from my tutorials and classes with code Institute.
## Content
* I got some of my recipes from [Github](https://www.allrecipes.com/).

## Media
* Some of the photos used in this site were obtained from :
1. [Unsplash](https://unsplash.com/).
2. [Pixels](https://www.pexels.com/).

## Acknowledgements
* I derived my inspiration for this project through my experience with the covid-19 lockdown, where i found myself browsing through multiple
cooking/recipe sites to find step by step cooking instruction on how to make meals and late night desserts which in normal times would have 
just been an eat out. This idea is targeted at creating a social platform where people connect and share their ideas on everything food!
 