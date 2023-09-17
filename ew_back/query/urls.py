from django.urls import path


from . import api

urlpatterns = [
    path('', api.search, name='search'),
    path('profile/<str:name>/', api.profile, name='profile'),
    path('test/', api.test, name='testing')

]