from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout
from .models import Run, userFrends, runLocations
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
import json
import ast 
import datetime
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import ast

def index(request):

    return render(request, "run/index.html")


def login(request):

    return render(request, 'run/login.html')


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_auth(request, user)
        return HttpResponseRedirect("/")
    else:
        context = {
            'error': 'wrong'
        }
        return render(request, 'run/login.html',context)



def logout_request(request, error='none'):
    logout(request)
    response = redirect('/')
    return response


def dashbord(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login")
    current_user = request.user
    test = Run.objects.filter(user=current_user.id).order_by('start_Time')
    output = {}
    refriends = {}
    refriendRequest ={}
    for i in range(len(test)):
        output[str(i)] = {'id':str(test[i].id),'distance': str(test[i].distance), 'start_time': str(
            test[i].start_Time), 'end_time': str(test[i].end_time), 'user': str(test[i].user) ,'everageSpeed':str(round(float(test[i].distance) /float(((test[i].end_time-test[i].start_Time).total_seconds())),2))}
    friends = userFrends.objects.filter(user=request.user)
    friendRequest = userFrends.objects.filter(frend=request.user)
    if len(friends) > 0:
        for i in range(0,len(friends)):
            if friends[i].status == 'dn':
                status = 'decline'
            if friends[i].status == 'ap':
                status = 'approved'
            if friends[i].status == 'pn':
                status = 'pending'

            refriends[str(i)] = {'friend':friends[i].frend.first_name,'status':status}

    if len(friendRequest) > 0:
        for b in range(0,len(friendRequest)):
            if friendRequest[b].status == 'dn':
                status = 'decline'
            if friendRequest[b].status == 'ap':
                status = 'approved'
            if friendRequest[b].status == 'pn':
                status = 'pending'

            refriendRequest[str(b)] = {'friend':friendRequest[b].user.first_name,'status':status}

    context = {
        'Runs': output,
        'friends': refriends,
        'friendReuest': refriendRequest
    }
    return render(request, "run/Dashbord1.html", context)


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
            )
        user.save( )
        login_auth(request, user)
    return HttpResponseRedirect("/")

def contact(request):
    return render(request , "run/ContactUs.html")

def run(request):
    return render(request, 'run/run.html')

def finishrun(request):
    run = json.loads(request.GET.get('run'))
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(run)
    args = run['startDate'].split(',')+run['startTime'].split(',')
    start = datetime.datetime(int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]),int(args[5]))
    args = run['endDate'].split(',')+run['endTime'].split(',')
    end = datetime.datetime(int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]),int(args[5]))
    foo = Run(distance=run['distance'],start_Time=start,end_time=end, user=request.user)
    foo.save()
    return JsonResponse(run)

def friends(request):

    
    return render(request, 'run/friends.html')

def send_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        note = request.POST.get('note')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        username = request.user.username
        friend = User.objects.filter(email = email).first()

        foo = userFrends(status = 'pn', user = request.user, frend = friend)
        foo.save()
        message = f"""{username} whants to be your friend on the running app \n
        this is a personal note from him:{note}\n 
        if you accsept this invetation please click this link :\n
        HTTPS://alexkotliar.com/accept/{foo.id} \n
        to dicline this request click here : \n
        HTTPS://alexkotliar.com/decline/{foo.id} \n
        
        thank you for using the running app \n
        
        """
        send_mail( 'You have a new Friend request in the running app',message , email_from, recipient_list )
        print(foo.id)
            
        
    
    return HttpResponseRedirect("/")

def accept(request, request_id ):
    print('laksjdhgflaksjdflikasjdhf;lkamshdflkjasdlfkjhasdlifhgasldjkhfgasjdyfgaisdbfkajhsd')
    print(request_id)
    foo = userFrends.objects.filter(pk=request_id).first()
    foo.status = 'ap'
    foo.save()

    return HttpResponseRedirect("/")

def decline(request, request_id):
    foo = userFrends.objects.filter(pk=request_id).first()
    print('laksjdhgflaksjdflikasjdhf;lkamshdflkjasdlfkjhasdlifhgasldjkhfgasjdyfgaisdbfkajhsd')
    print(request_id)
    foo.status = 'dn'
    foo.save()
    return HttpResponseRedirect("/")

def GetFriendStat(request):
    fname = request.GET.get('user')
    current_user = User.objects.filter(username = fname).first()
    test = Run.objects.filter(user=current_user.id).order_by('start_Time')
    output = {}
    for i in range(len(test)):
        output[str(i)] = {'distance': str(test[i].distance), 'start_time': str(
            test[i].start_Time), 'end_time': str(test[i].end_time), 'user': str(test[i].user)}

    return JsonResponse(output)

def changeStatus(request):
    if request.method == 'POST':
        username = request.POST.get('UserNameToChange')
        newStatus = request.POST.get('status')


    user = User.objects.get(username = request.user)
    friend = User.objects.get(username = username)
    foo = userFrends.objects.filter(user = user, frend=friend).first()
    if newStatus == 'Pending':
        foo.status = 'pn'
        foo.save()
    if newStatus == 'Dicline':
        foo.status = 'dn'
        foo.save()
    if newStatus == 'Approve':
        foo.status = 'ap'
        foo.save()

    return HttpResponseRedirect("dashbord")

def FriendVerification(request):
    params = request.GET.get('email')
    resolt = {}
    foo = User.objects.filter(email=params).first()
    foofoo = userFrends.objects.filter(user=request.user, frend=foo).first()
    if foo != None:
        if foofoo == None:
            resolt['status'] = 'good'
        else:
            resolt['status'] = '2'
    else:
        print('faild 1st condition')
        resolt['status'] = '1'
    foofoofoo = User.objects.filter(username=request.user).first()
    if foo == foofoofoo:
        resolt['status'] = '3'
    
    return JsonResponse(resolt)


def sendLocationPointes(request):
    resolt = {}
    params = request.POST.get('locations')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(params)
    user = User.objects.get(username=request.user)
    runID = Run.objects.filter(user = request.user).order_by('-id')[0]
    foo  = runLocations(user=user, locations=params,runID = runID)
    foo.save()
    resolt['status'] = 'good'
    return JsonResponse(resolt)


def getlocations(request):
    resolt = {}
    params = request.POST.get('runid')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(params)
    foofoo = Run.objects.get(pk = int(params))
    foo = runLocations.objects.get(runID = foofoo)
    locations = foo.locations
    print(locations)
    locations = ast.literal_eval(locations)
    resolt['status'] = 'good'
    resolt['locations'] = locations
    return JsonResponse(resolt)



def changeStatusFriend(request):

    if request.method == 'POST':
        username = request.POST.get('UserNameToChange1')
        newStatus = request.POST.get('status')
        user = User.objects.get(username = request.user)
        friend = User.objects.get(username = username)
        foo = userFrends.objects.filter(user = friend, frend=user).first()
        if newStatus == 'Pending':
            foo.status = 'pn'
            foo.save()
        if newStatus == 'Dicline':
            foo.status = 'dn'
            foo.save()
        if newStatus == 'Approve':
            foo.status = 'ap'
            foo.save()

    return HttpResponseRedirect("dashbord")