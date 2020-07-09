from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.get_entry, name="entry"),
    path("search",views.search,name="search"),
    path("create", views.create, name="create"),
    path('check_entry', views.check_entry, name="check_entry"),
    path('edit', views.edit, name='edit'),
    path('edit_submit', views.edit_submit, name="edit_submit"),
    path('random', views.random, name='random')
]
