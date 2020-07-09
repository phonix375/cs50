"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('run.urls')),
    path('login', include('run.urls')),
    path('logout', include('run.urls')),
    path('logincheck', include('run.urls')),
    path('dashbord', include('run.urls')),
    path('register', include('run.urls')),
    path('contact', include('run.urls')),
    path('run', include('run.urls')),
    path('finishrun', include('run.urls')),
    path('send_request', include('run.urls')),
    path('GetFriendStat', include('run.urls')),
    path('changeStatus', include('run.urls')),
    path('FriendVerification', include('run.urls')),
    path('sendLocationPointes',include('run.urls')),
    path('getlocations', include('run.urls')),
    path('changeStatusFriend', include('run.urls'))
]
