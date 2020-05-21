# SchedulingApi
api to schedule the task after matching current date and time

project setup :- 
1- create a folder SchedulingApi in your computer 
2- create a virtual enviroment for your project.You can create virtual enviroment in your current folder 
   by simple typing in your terminal.
   
$ python3 -m venv env

3- install django in your virtual env .

$ pip install django

4- install django rest framework in your env .
$ pip install djangorestframework

after installing django and django rest framework let's create a django project "api" by typing following commond in your terminal

$ django-admin startproject api .

this will add a folder named api and a manage.py folder in your project directory.

goto your api folder and create a new file views.py in it .

before doing anything else make sure you add  rest framework in installed  apps under setings.py file of your api.


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

now open views.py file to create api view for our project.
add the following lines in views.py:

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
import datetime


@api_view(['GET'])
def pingEndpoint(request):
    '''
        return the respone 200 ok if server is alive
    '''
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def apiEndpoint(request,*args,**kwargs):
    '''
        take current date and time from user and schedule the task if the date and time match 
        with current server date and time 
    '''

    try:
        DateTime=datetime.datetime.now()
        Date,Time = str(DateTime).split()

        if (kwargs['date'] == Date) and (kwargs['time'] == Time[:5]):

            return Response(f'task is scheduled at {kwargs} ',status=status.HTTP_201_CREATED)

    except Exception as e:
        raise APIException(str(e))
        
        
 let's break the code little bit , here we first import some required library to create api views
 we import api_view decorater to make the view as api,
 
 the Response is used to return jason response to the browser and,
 status is used return current status of your api.
 
 then we create a function named ping which will check about our server status and if server is alive it will send a response of 
 200 OK .
 
 then we add another function apiEndpoint which will get the request from server and current date and time .
 this function will send response to the browser if the request date and time match with current date time and create a schedule of it
 
 
 Now after doing this let's make url for our views , to do this go to urls.py file of your api folder .
 
 now add the following code to it :
 
 
from django.contrib import admin
from django.urls import path,re_path
from .views import pingEndpoint,apiEndpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/',pingEndpoint),
    re_path(r'^(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/(?P<time>[0-9]{2}:?[0-9]{2})$', apiEndpoint),
]

it will create url endpoints for our api which will handle our requests.

Now its time to check our api , to do this go to your terminal and type following commonds.
first we have to migarte our project to do this type following commond 
$ python manage.py migrate.

now its time to run our server by typing just typing the following commond :
$ python manage.py runserver

if all things gone right it will show you following lins in your terminal :

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 21, 2020 - 10:09:57
Django version 3.0.3, using settings 'api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Good! now its time to check our api .

goto your web browser and type the given link to check your server status:

http://127.0.0.1:8000/ping 

it will lead you to a page showing the status as 200 OK.

Great!

Now let's check our apiEndpoint just type given link with current date and time like  :
http://127.0.0.1:8000/2020-05-21/22:10

after hitting enter it will show a jason respone which gives you the current date and time saying your task is scheduled as given formate

HTTP 201 Created
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

"task is scheduled at {'date': '2020-05-21', 'time': '10:17'} "

that's it we make it!

now stop your local server by typing clicking "ctrl+c" in your terminal.




 
 
 
 
 

   
