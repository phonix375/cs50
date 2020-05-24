# Project 4 - Final Project by Alexy Kotliar - May 24, 2020

the goal :
build a fitness tracker application for people who like to run and want to see the history and improvement and performers, and who like to compete with there friends 

The technologies  : 
the application was built with CSS Grid system and bootstrap for mobile responsiveness, GeoLocation for location, and google maps API for map representation, Python for backend programming with Django framework, javascript, HTML, CSS on the front end and Chart.js for the charts.
because this application was using GEOlocations I uploaded this application to amazon server EC2 instance with domain : 
https://alexkotliar.com
as all browser applications that use GeoLocation have to be with SSL certificate, and I'm using free "let's encrypt " certificate 

log-in/ register :
using Django authentication and Javascript all the fields in the login/register options are check with JavaScript to see if the content is valid before there is an option to submit the form and log-in or register using Django build-in authentication.

The Dashboard : 
in the dashboard the user has 3 options : 
	*dashboard
	*new Run
	*friends

*dashboard - the user can see a chart with a history of his run's, by default the chart is set by distance X axle is ordered date and the Y is the distance, on the top of the chart there is an option to select the chart by average speed when this option is selected another filter will appear with a selection of distance 

*new Run - selecting this option will get a menu where the user can select the distance he wants to run and start and stop buttons. 
clicking the start button will start a timer (javascript interval) and will call get geolocation, every point from there is saved in a list and a function calculates the price is returning the distance between the last point and a current one and adding this to a global variable distance until the user reaching the selected distance after the goal is reached 2 AJAX request are made 2 to save the run and another to save the locations.
this section is made for mobile phones as I'm using accurate location option from geoLocation to get GPS coordinates and not cell tower or IP


*friends - in this section the user can see all his friend requests he sent or was sent to him and a Form to send a new friend request.
the form is checked with python to make sure there is a user with this email and there was no other request between these users.
after the user is sending a friend request, his friend receives an email with 2 links to accept or decline the friend request, I'm using the friend request-id in the /accept or /decline URL to execute the request.
after the friend request was sent the user has the option to accept in the friend section in the dashboard as well.
after a friend request is accepted, there will be a link in the friend section to view the friend's statistics.
