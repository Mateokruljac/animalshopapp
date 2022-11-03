from datetime import datetime
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.http import JsonResponse 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from pets.models import Animal
from members.models import Customer,Order,OrderItem
from pets.utils import cart_total_quantity
import json
# Create your views here.

#create customer account
def user_register(request):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]

    if request.method == "POST":
         #user info 
         firstName = request.POST.get("firstName")
         lastName = request.POST.get("lastName")
         username = request.POST.get("username")
         email = request.POST.get("email")
         password = request.POST.get("password")
         confirmPassword = request.POST.get("confirmPassword")
         # if checkbox is not  clicked, buttonAgree will get None.
         buttonAgree = request.POST.get("checkbox")
         print("ButtonAgree",buttonAgree)
         
         #check user info
         if password == confirmPassword:
            if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists(): # if exists, return True
               messages.info(request,"User with that username or email alredy exists!")
               return render (request,"register.html",{"cart_items":cart_items})
            else:
                if buttonAgree is not None: 
                    user = User.objects.create_user(
                        first_name = firstName,
                        last_name = lastName,
                        email = email,
                        username = username, 
                        password = password
                    ).save()
                    return redirect("customer_login")
                    
                else:
                   messages.info(request,"Please, accept all statements in Term of services. Thank you!")
                   return render (request,"register.html",{"cart_items":cart_items})
                
                    
         else:
             messages.info(request,"Passwords not matching!")
             return render (request,"register.html",{"cart_items":cart_items})
             
    else:   
       return render (request,"register.html",{"cart_items":cart_items})
   
   
   

#customer login 
def user_login(request):
    context = cart_total_quantity(request)
    cart_items = context["cart_items"]
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password)
        user = authenticate(username = username, password = password)
        print("User",user)
        if user is not None:
            login(request,user)
            #if logged in user already has customer account, try block will be correct and view is going to redirect to store
            # if logged in user hasn`t customer account, except block will be activated and view is going to create a customer account.
            try:
                request.user.customer
            except:
               return  redirect("customer")
            else:
               return  redirect("store")
            
            # animals  = Animal.objects.a4ll()
            # return render (request,"core/store.html",{"animals":animals})
        else:
            messages.info(request,"Invalid username or password!")
            return render (request,"login.html",{"cart_items":cart_items})
    else:    
      return render (request,"login.html",{"cart_items":cart_items})
  
  
def user_logout(request):
    logout(request)
    return redirect("customer_login")

#create customer page
def customer_page(request):
    user = request.user
    email = request.user.email
    name = request.user.username
    
    if Customer.objects.filter(user = user, email = email, name = name).exists():
        return redirect ("store")
    else:
        customer = Customer.objects.create(user = user, email = email, name = name)
        customer.save()
        return redirect("store")
    

#customers action


def update_item(request):
    data = json.loads(request.body)
    product_id = data["productID"]
    action = data["action"]
    print("Product id",product_id)
    print("Product id",action)
    
    customer = request.user.customer
    product = Animal.objects.get(id = product_id)
    order,created = Order.objects.get_or_create(customer = customer,complete = False)
    order_item,created = OrderItem.objects.get_or_create(product = product,order = order)
    
    if action == "add":
        order_item.quantity += 1
    if action == "remove":
        order_item.quantity -= 1
    
    #save change
    order_item.save()
    
    if order_item.quantity <= 0:
        order_item.delete()
        
    
    return JsonResponse("Item was added",safe = False)

def proccess_order(request):
    transaction_id = datetime.now().timestamp() #it won`t be same for each order
    data = json.loads(request.body)
    total = data["userTotal"]["total"] #float format
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer,complete = False)
        order.transaction_id = transaction_id
        
        order.complete = True
        order.save()
    return JsonResponse("Payment Done",safe = False)