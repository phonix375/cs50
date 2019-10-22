# Project 1

Web Programming with Python and JavaScript
Project1 by Alexy Kotliar 22 Oct 2019
Book review web application build with Python flask, html , and postgres SQL

Login page:
On the main page is the login page where you can login with existing user name or register 
The application checks if the user name and password are correct and redirect you to the search page if it is 
And if not redirect you to an error.html with an error 'the user name or password is incorrect'

Register page:
On the register page you i ask the user to select a user name and a password and 2 optional parameters are full name and email 
of if the user have a full name it will be displayed at his review and if he don’t have a full name just an email then the email will be displayed and if the user don’t have it then the user name will be displayed.
The register page also checks if user with the same user name exist, and if it does redirect you to a error.html with an error 'user name exist please select another'.

Search page: 
On the search page if a user try to access it and he is not logged in he will be redirected to error.html with the error 'please login to search ‘.
If the user is logged in in the nav bar he will have the option to log out.
In the search page user have 4 options to search by: isbn, author, title and year.
the search use LIKE % % so you can search by partial name and it’s not key sensitive so you can search for uppercase and lower case letters.

book page : 
Here I’m using goodreads.com API to display Average rating , number of reviews and number of ratings on goodreads.com . 
You have the option to write a review for this book , the application check if you already did a review for this book , if yes it will redirect you to error.html with the error ‘you already reviewed this book ’ and if not you will be redirected back to the same book page and you will see your review on the bottom of the page .

API : 
To use the api of the application you don’t have to be logged in, just use ‘/api/ISBN’ where isbn is the isbn of the book and if the book exist in by data base you will get json object with the information for this book , if the isbn don’t exit it the data base you will receive json object with error 403 
