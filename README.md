# Project 2

Web Programming with Python and JavaScript
Project2 by Alexy Kotliar 06 Dec 2019
Chat application build with Python flask, html , Javascript, soketIO

when going to the page for the first time you promped to enter a user name that will be on every message that a user sends
and if you trying to enter a user name that alrady exist you will see a message asking to select another user name .

chat room page : 
on the left side you will see a list of all chat rooms and a form to add a new chat room , if you will try to enter a chat room that
alrady exist it will alert you to select a difrent name for your chat .
when sending a message in a chat room, every message is displayed in a bootstrap card with a title including user name that sent the message and the time stamp when the message was sent . 

closing the application :
after login I'm storring the user name in localSstorage and the room you are in so the next time you visit the application it wont promt you to enter a user agin and just load from local storage and take you back to the same room you was in before closing the application. 

logout : 
on the top of the chat room there is an option to log out from the chat so I'm deleting the localStorage for user name and the next time you will go to the chat you will be prompt to enter user name agin .

personal toch : 
in the chat by the message form you have an option to send a picture as a message , the image will get uploaded to the application with a generated name so you can send the same image number of times.
