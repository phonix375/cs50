# Project 0

Web Programming with Python and JavaScript
Project0 by Alexy Kotliar 09/24/19
Subject selected : my home city of Fredericton, New Brunswick, Canada.
The website contains 4 pages: News, Things to do, History and contact us 
As navigation for this project I used bootstrap 4 <nav> element in every page to navigate to every page and when on small screen size the menu collapse to a “burger” menu.and every page uses the same logo with id “logo” to style it and <footer> , all the elements styled by style.css . 
On the first page index.html is the news page , I used bootstrap 4 grid system so on a large screen it will present 3 news card , in the news card I used class “card” and to scale the <img> I used the class “cardimage”.
On the second page “Things to do” I used another bootstrap element carousel with navigation to display images with control , to style and position the carousel I used  id “myCarousel” .
In the table on the “Things to do” I used @media tag to change the size of the table depending on the screen size , and used the ::before and ::after selectors to input content in front and after the table .
On the History page I used the bootstrap 4 grid just for one container , used a <a> tag and unordered list inside a unordered list .
On the “contact us” page I used the bootstrap grid system and <img> for the logos .
Requirements : 
•	Your website must contain at least four different .html pages, and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.
My website have 4 pages : news, Things to do, History and contact us
•	Your website must include at least one list (ordered or unordered), at least one table, and at least one image.
on page “History” I used an unordered list inside unordered list and on page “Things to do” I used a table and on page “news” I used images
•	Your website must have at least one stylesheet file.
My website contains style.css
•	Your stylesheet(s) must use at least five different CSS properties, and at least five different types of CSS selectors. You must use the #id selector at least once, and the .class selector at least once.
My style.css properties: width, margin, border, text-align, color and more
My style.css selectors : id, table, ::before, ::after , footer and more
•	Your stylesheet(s) must include at least one mobile-responsive @media query, such that something about the styling changes for smaller screens.
On page “Things to do” I use @media for resizing the table on a small screen 
•	You must use Bootstrap 4 on your website, taking advantage of at least one Bootstrap component, and using at least two Bootstrap columns for layout purposes using Bootstrap’s grid model.
On page “news” and “contact us” I use the grid with bootstrap and on all pages I use bootstrap navigation and on “Things to do” page I use the carousel from bootstrap 4
•	Your stylesheets must use at least one SCSS variable, at least one example of SCSS nesting, and at least one use of SCSS inheritance.
In style.scss I’m using 3 variables for colors , on page “Things to do” I use the nesting for the table and im using inheritance for font family on the “news“ page and “Things to do” page
•	In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project.


