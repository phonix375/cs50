from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout_request, name='logout'),
    path('logincheck',views.login_view, name="logincheck"),
    path('register',views.register_view, name="register"),
    path('dashbord', views.dashbord, name="dashbord"),
    path('contact', views.contact, name="contact"),
    path('run', views.run, name="run"),
    path('friends', views.friends, name='friends'),
    path('send_request', views.send_request, name='send_request'),
    path('finishrun', views.finishrun, name='finishrun'),
    path('accept/<int:request_id>', views.accept, name='accept'),
    path('decline/<int:request_id>', views.decline, name='decline'),
    path('GetFriendStat', views.GetFriendStat, name='GetFriendStat'),
    path('changeStatus', views.changeStatus, name='changeStatus'),
    path('FriendVerification' , views.FriendVerification, name='FriendVerification'),
    path('sendLocationPointes', views.sendLocationPointes, name='sendLocationPointes'),
    path('getlocations', views.getlocations, name='getlocations'),
    path('changeStatusFriend',views.changeStatusFriend, name='changeStatusFriend')
]
