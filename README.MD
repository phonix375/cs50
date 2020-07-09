# final project by Alexy kotliar 09-07-2020
The Running app  -
Background:
This project is using JavaScript GEO location so to test this app it needed to be deployed on server and a domain with SSL certificate,
so I created an EC2 instance on ubuntu with free SSL from let’s encrypt.

App goal : 
This is a running app for people who like to run and compete against others to improve themselves,
in this app the users have the option to record a run, see the history of all runs they did and to add friends who use this app as a friend,
then they will have the option to compare the results. 

App description : 
When a user visits the website for the first time he will have the option just to login and see the main page with some information about the app,
the main page and the login/register pages where build with responsive CSS grid to create this style.

login\register : 
in this page I'm using JavaScript to make sure the user is entering the correct information to the forms before he have the option to submit the form.
After the user is login, he will have 2 more option on the main page – logout and dashboard

The dashboard – this is the main page of the application, here on the main dashboard the user can see his statistics and change the view from distance graph to average Speed,
this graph is build with JavaScript graph library.
Under the graph the user will see a table with all the runs he did with start and end time as well as average speed
and a button to see the run where I used google map API to display the running path using the GEO location I collect during the run.

Start new run – in this section of the dashboard the user can start a new run by selecting the distance he wants to run and clicking start,
every 2 seconds I’m recording the new GEO location point and calculating the new distance, ignoring points that creating an impossible speed.
After the distance is reaching the selected distance, the user will get an alert of completion and the run will be added to his list of runs.

Friends – in this section the user have the option to send a friend request to another user of the app by email,
when the user is sending the request the other person will receive an email with the friend request with 2 options: to accept or reject the request.
The link that the user is receiving consist of accept/<request-id> and reject/<request-id> by cliking the link you can accept or reject,
or another option is to login to his “RUNNING APP” account go to the friends section in the dashboard,
and the user will see the option to accept or reject the invitation as well as an option to  cancel friendship after its accepted.

Technologies from the course I used : 
HTML, JavaScript, Python, Django + Templates , CSS, SQLite
