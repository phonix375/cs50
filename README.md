# Contract Sign, By Alexy Kotliar
#### Video Demo:  https://www.youtube.com/watch?v=BcXVUb7bX38
#### Description:
This is a web application for a business that offers multiple Services, and need to send a unique set of contracts to each customer. In the web application, the owner will have the option to add new contacts delete contracts, and generate a unique link to send to the client.

#### Structure of the application:
app.py - this is the main flask server file with all the routes and imports of libraries I'm using :
From the Flask libraries I'm importing flask - to work with the application, request to receive requests from the front end, redirect to send the user to another route, session to save the user name so I will be able to check if the user is logged in or not. I'm decided to use SQLAlchemy in my project, to simplify the work with the database. to achieve this I created the model in the models.py file, with classes of all my tables in the database.

Front end - On the front side of the application I created the main template with the main navigation menu, in this menu depends on if the user logged in or not I will display different options. the list of templates I'm using :
- Contract.html: used to display the contract
- error.html: every time I'm detecting an error like the wrong user name or password, I'm redirecting the user to the error page and passing the error message to display to the user.
- Home.html: this is the first page when the user is getting to the website, in this page I'm displaying the name of the user is logged in or none if the user is not logged in
-login.html: on this page, I'm showing giving the user the option to log in.
-my_forms.html: This is the main file for a logged-in user to see all of their contracts, edit or delete contacts, and the option to create a new contract and generate a link to clients with the relevant contracts to this client.
-settings.html: in this file, I'm giving the logged-in user the option to upload his latter head to the application to be added to all his contracts.
-sign.html: this is the page that the clients of the user will access to see their contracts without the need to log-in.
-template.html: in this file, there is the main menu that will be on every page.


API - In this project, I'm using Tiny API to give the user the option to edit the contract with a simple editor and without the need to write HTML code.

Login/register - for the login and register I'm using hashing to save the user name password for security
Generate link- Using python UUID I'm generating and unique link for every link to documents so there will be no duplicates.



