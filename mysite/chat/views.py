from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from operator import itemgetter, attrgetter, methodcaller 

# Create your views here.
# chat/views.py

#def index(request):
#    return render(request, 'chat/index.html')

#def room(request, room_name):
#    return render(request, 'chat/room.html', {
#        'room_name': room_name
#    })

@login_required
def briefingRoom(request):
    return render(request, 'chat/room.html', {
        'room_name': 'briefing',
        'user_id': request.user.id,
        'username': request.user.username,
    })