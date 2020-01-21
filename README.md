# Project 3

The requirements  : 
menu : 
when visiting the web site even if the client is not logged in he will be able to view the menu, and the menu is generated from the database so if the owner will make a change or add/remove an item it will be reflected in the menu.
Adding items 
from the admin panel, you can add items to the "MenuItem" table with the price of the item, category, and a large price if available for that item. from the same table, he can update an existing item or delete it.
Registration, Login, Logout 
using DJANGO's authentication a client can register login and logout from the website. after the registration, the client will receive an email with his user name and password. after the client is logged in he will be able to see the full Main menu with the shopping cart and order history.
Shopping Cart
after the client adds an item to the shopping cart I'm using BOOTSRAP's badge to show the number of items in the shopping cart. ones the client clicks on the shopping cart he can see the items with the toppings he as selected and the full price of all the items. the shopping cart is pulling the information from local storage so even if the client logs out or closes the website when he returns to the site he still will have all the items there.
Placing an order 
In the shopping cart, the client can see the option to confirm the order, ones the order is confirmed the shopping cart deletes all the items and deletes the items from local storage as well and the badge on the cart goes to 0. ones an order is placed the client will receive a conformation email with the order details.
Viewing Orders 
In the main menu after the client log-in, he will have the options to view all his orders, including the ID or the order, items, toppings, and status of the order. this will be a list of all the confirmed orders.
Personal touch 
As a personal touch, I did all the menus of the page to be popup forms and after registering on the website you will receive an email Thanking the client for registering and the information about the account with user name and password as well as after completing a new order the client will get an email with the details of the order.

Models : 
users - I'm using DJANGO authentication system 
menuItems - a table with the items name price and category
Orders - contain the order id, user and manyTomany of orderItems
OrderItems - the items with the options that the client selected
Toppings - a list of all available toppings 

