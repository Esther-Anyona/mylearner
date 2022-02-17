# Myblog
<hr>
## Author
[Esther-Anyona](https://github.com/Esther-Anyona)
<hr>
[Live link](https://star-blog1.herokuapp.com)

## Description
This is a python flask application that allows users to post blogs, edit and delete blogs. It also requires users to sign up in order to comment on other users' posts as well as edit and comment on their own posts. on sign up, a user receives a welcome email. Users create their own profiles which they can update at any time.

## Screenshot
[Myblog homepage](app/static/photos/myblog1.png)

## User Stories
* A user can view the most recent posts.
* View and comment on any post on the site.
* A user should receive an email alert after successful signup.
* Registration is mandatory to be allowed to log in and interact with the application features.
* A user sees random quotes on the site every time the page refreshes
* A writer can create a blog from the application and update or delete blogs I have created.

## BDD
1. On Loading the homepage - view all blog posts, see a random quote, select between signup and login.
1. If Select SignUp, form opens to enter registration details i.e. Email,Username,Password and Password confirm. Then Redirect to login page
1. Existing users select Login and enter Username and Password, they are then redirected to homepage with their profiles active.
1. If one wants to update profile - Select profile and they are redirected to upload profile photo and edit bio.
1. Comments button for adding a new comment or viewing the existing comments.

### Installation Requirements
* Python3.8
* Flask 2.0.2
* gunicorn
* pip
* SQLAlchemy

### Cloning
* Run $ git clone https://github.com/Esther-Anyona/mylearner.git on your terminal

### Running the Application
After cloning, in the terminal: 
* $ cd to the project directory
* $ python3 -m venv virtual - to create a virtual environment
* $ source virtual/bin/activate - to activate virtual environment
* $ pip install flask
* $ Install flask extensions
* $ python manage.py test - to run tests
* $ ./start.sh to execute
* $ Open the application on your browser 127.0.0.1:5000 to view

### Technologies used
* Python3.8
* Flask 2.0.2
* Bootstrap v5
* SQLAlchemy postgresql

### Contacts
You can reach me through:
* Email: jkemuntoe@gmail.com or
* Phone: +254724374477

## License
*MIT License*:
Copyright (c) 2022 *Esther Anyona*