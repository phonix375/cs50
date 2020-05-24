from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
#for adding userse
from django.contrib.auth.models import User
from .models import menuItem, Topings, orders, orderItem
import json
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request, error='none'):
    if not request.user.is_authenticated:
        context = {
            'user' : 'none',
            'menuItems' : menuItem.objects.all(),
            'topings' : Topings.objects.all(),
            'error' : error
        }
        return render(request,'pizza/index.html', context)
    else:
        context ={
            'user' : request.user,
            'menuItems' : menuItem.objects.all(),
            'topings' : Topings.objects.all(),
            'error' : 'none'
        }
        return render(request,'pizza/index.html', context)


def login(request):
    return render(request, 'pizza/login.html')

def menu(request):
    context = {
        'menuItem': menuItem.objects.all(),
        'Topings' : Topings.objects.all()
    }
    return render(request, 'pizza/menu.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None : 
        auth_login(request, user)
        response = redirect('/')
        return response
    else :
        context = {
            'user' : 'none',
            'menuItems' : menuItem.objects.all(),
            'topings' : Topings.objects.all(),
            'error' : 'Incorrect User name or password'
        }
        return render(request,'pizza/index.html', context)



def logout_view(request):
    logout(request)
    response = redirect('/')
    return response

def register(request):
    userName = request.POST['userName']
    password = request.POST['password']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']

    user= User.objects.create_user( username= userName,email=email,password =password,first_name =firstName,last_name= lastName )
    user.save()


    subject = 'Thank you for registering to our site'
    message = f'Thank you {firstName} {lastName} for registering for our Pizzeria Use your User name: {userName} and password : {password} to log in to our website and make orders '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )

    response = redirect('/')
    return response


def gettopings(request):
    item = menuItem.objects.get(id=request.GET.get('itemId'))
    topimg = Topings.objects.filter(toping=item.toping)
    aList = []
    for value in topimg :
        aList.append(value.name)

    if item.large != 0 : 
        large_price = item.large
    else :
        large_price = 0
    data = {
        #'data': request.GET.get('itemId')
        'data' : aList,
        'price': item.price,
        'large' : large_price
    }
    return JsonResponse(data)


def order(request) :              
    response = redirect('/')
    res = json.loads(request.GET.get('order'))
    order = orders(user = User.objects.get(username=request.user.username).username)
    order.save()
    y = 1
    emailOrder = {y :''}
    for x in res :
        item = menuItem.objects.get(name=x['item'])
        size = x['size']
        emailOrder[y] = x['item'] + ' - ' + x['size'] + ' '
        foo = orderItem(item=item,size=size)
        foo.save()
        order.orderItems.add(foo)
        if len(x['topings']) != 0 :
            for i in x['topings']:
                toping = Topings.objects.get(name=i)
                foo.topings.add(toping)
                foo.save()
                emailOrder[y] += ' ' + i + ' '
        else:
            emailOrder[y] += ' no Topings '
        y += 1
    order.save()

    userName = request.user.username
    firstName = request.user.first_name
    lastName = request.user.last_name
    email = request.user.email
    subject = 'Thank you for Ordering From Pizza CS50'
    message = f'Thank you {firstName} {lastName} your order : {str(emailOrder)} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )

    data = {'blat': res}
    return JsonResponse(data)



def myorders(request):
    myOrders = {'orders':{}}
    dictOforders = {}
    ordersList = orders.objects.filter(user=User.objects.get(username=request.user.username))
    for i in ordersList :
        myOrders['orders'][f'{i.id}'] = {'items':[]}
        for y in i.orderItems.all():
            topingList = []
            for x in y.topings.all():
                topingList.append(x.name)
            myOrders['orders'][f'{i.id}']['items'].append({'name':y.item.name, 'size' :y.size, 'topings':topingList})


        
        myOrders['orders'][f'{i.id}']['status'] = i.status

    data = myOrders
    return JsonResponse(data)



def adminPanel(request) : 
    myOrders = {'orders':{}}
    dictOforders = {}
    ordersList = orders.objects.filter(user=User.objects.get(username=request.user.username))
    for i in ordersList :
        myOrders['orders'][f'{i.id}'] = {'items':[]}
        for y in i.orderItems.all():
            topingList = []
            for x in y.topings.all():
                topingList.append(x.name)
            myOrders['orders'][f'{i.id}']['items'].append({'name':y.item.name, 'size' :y.size, 'topings':topingList})


        
        myOrders['orders'][f'{i.id}']['status'] = i.status

    data = myOrders
    context ={
            'user' : request.user,
            'menuItems' : menuItem.objects.all(),
            'topings' : Topings.objects.all(),
            'error' : 'none',
            'orders' : data
        }
    return render(request,'pizza/adminPanel.html', context)


def getAllOrders(request):
    myOrders = {'orders':{}}
    dictOforders = {}
    ordersList = orders.objects.all()
    for i in ordersList :
        myOrders['orders'][f'{i.id}'] = {'items':[], 'user': i.user}
        for y in i.orderItems.all():
            topingList = []
            for x in y.topings.all():
                topingList.append(x.name)
            myOrders['orders'][f'{i.id}']['items'].append({'name':y.item.name, 'size' :y.size, 'topings':topingList})


        
        myOrders['orders'][f'{i.id}']['status'] = i.status

    data = myOrders
    return JsonResponse(data)