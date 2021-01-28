# Contract Sign, By Alexy Kotliar
#### Video Demo:  https://www.youtube.com/watch?v=BcXVUb7bX38
#### Description:
This is a web application for a business that offers multiple Services, and need to send a unique set of contracts to each customer. In the web application, the owner will have the option to add new contacts delete contracts, and generate a unique link to send to the client.

#### Structure of the application:
app.py - this is the main Flask server file. Here I'm using the session to check if the user is logged in or not, SQLAlchemy to simplify the work with the SQLite database, UUID to generate a unique URL for the client, passlib.hash to hash the passwords before saving them to the database and other standard libraries for Flask. In this file, I have all the routes for the application.
database - in this project, I created an SQLite database using SQLAlchemy with 3 tables: Users, Contracts, and links. In the models.py file, you can see the structure of the database.

Front end - on the front end I'm using AJAX to send information to the server and get information back without the need to reload the page and updating the content of the page using javascript to modify the elements

API - In this project I'm using Tiny API to give the user the option to edit the contract with a simple editor and without the need to write HTML code

Login/register - for the login and register I'm using hashing to save the user name password for security

Generate link- Using python UUID I'm generating and unique link for every link to documents so there will be no duplicates.