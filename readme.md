How to start:
    - git clone https://github.com/Mateokruljac/animalshopapp.git 
    - create your enviroment and activate it
    - install required packages
    - py manage.py runserver (running on localhost)
 
Install packages: 
   pip install (dajngo, djangorestframework, pillow, mysqlclient) 

Testing API: 
    - use Thunder Client


Description: 
     the homepage provides a list of animals that the user can buy. If the user is not registered, he will not be able to add the animal to the card, 
     but he will be notified that he must register. CRUD operations are also conditional on registration.If the user does not have an account, he should
     go to the regiter option and then he will be directed to login. When he logs in, if it is his first time, his account will be created automatically.
     On the home page, the user can view or access the detail page of individual animals, add them to the card, and create their own. Each page has access
     to the navigation panel. From it, he can perform the following actions: create tags and categories, edit if he is the creator, and he can see a list 
     of all existing ones. The user can also access car.html by clicking on the cart icon. On that page, the user can see his selection, change the quantity,
     see the existing one and see the price. If he wants, he can go back to shopping, and he can continue to pay by clicking on checkout. If he chooses this
     option, he will go to checkout.html and get an overview of his order, as well as the fields for entering the address and then the payment button. After 
     he receives an alert that the transaction has been successfully completed, he is returned to the homepage and has the option to perform the previously mentioned actions.
