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
