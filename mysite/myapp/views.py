from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from operator import itemgetter, attrgetter, methodcaller
from django.core.mail import send_mail
from django.conf import settings

from . import models
from . import forms
import json

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            suggestion_form = forms.SuggestionForm(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save(request)
                suggestion_form = forms.SuggestionForm()
                return HttpResponseRedirect('/')
    else:
        suggestion_form = forms.SuggestionForm()
    suggestions_objects = models.suggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestions_objects:
        comment_object = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg ={}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["id"] = sugg.id
        temp_sugg["client"] = sugg.client.username
        temp_sugg["comments"] = comment_object
        suggestion_list+=[temp_sugg]

    #comments = models.CommentModel.objects.all()
    context = {
        "title":"suggestions",
        "suggestions":suggestion_list,
        "form":suggestion_form,

        #"comments":comments
    }
    return render(request, "index.html", context=context)

@login_required
def preperation(request):
    card = []#list[]
    for i in range(1, 10):#generate 9 cards
        if i == 1:
            card_dict = {
                "cardTitle": "Mercury Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Mercury Card #" + str(i),
                "counter": i 
            }
        elif i == 2:
            card_dict = {
                "cardTitle": "Venus Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Venus Card #" + str(i),
                "counter": i 
            }
        elif i == 3:
            card_dict = {
                "cardTitle": "Earth Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Earth Card #" + str(i),
                "counter": i 
            }
        elif i == 4:
            card_dict = {
                "cardTitle": "Mars Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Mars Card #" + str(i),
                "counter": i 
            }
        elif i == 5:
            card_dict = {
                "cardTitle": "Jupiter Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Jupiter Card #" + str(i),
                "counter": i 
            }
        elif i == 6:
            card_dict = {
                "cardTitle": "Saturn Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Saturn Card #" + str(i),
                "counter": i
            }
        elif i == 7:
            card_dict = {
                "cardTitle": "Uranus Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Uranus Card #" + str(i),
                "counter": i 
            }
        elif i == 8:
            card_dict = {
                "cardTitle": "Neptune Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Neptune Card #" + str(i),
                "counter": i 
            }
        else:
            card_dict = {
                "cardTitle": "Pluto Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Pluto Card #" + str(i),
                "counter": i 
            }
        card.append(card_dict)

    title = "Know Your Planet"
    context = {
        "title":title,
        "card":card,
    }
    return render(request, "preperation.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

@login_required
def get_suggestions(request):
    suggestion_objects = models.suggestionModel.objects.all()
    suggestion_list = {}
    suggestion_list["suggestions"] = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg ={}
        temp_sugg["suggestion"]=sugg.suggestion
        temp_sugg["client"]=sugg.client.username
        temp_sugg["id"]=sugg.id
        temp_sugg["comments"]=[]
        for comm in comment_objects:
            temp_comm={}
            temp_comm["comment"] = comm.comment
            temp_comm["id"] = comm.id
            temp_comm["client"] = comm.client.username
            temp_sugg["comments"]+=[temp_comm]
        suggestion_list["suggestions"]+=[temp_sugg]
    return JsonResponse(suggestion_list)

@login_required
def compete(request):
    title = "Space Trivia"
    content = "Welcome to my work in progress!(compete)"
    context = {
        "title":title,
        "body":content,
    }
    return render(request, "compete.html", context=context)

@login_required
def game(request):
    scores = models.Profile.objects.all()
    title = "Competition"
    content = "Welcome to my work in progress!(game)"
    context = {
        "title":title,
        "body":content,
        "scores":scores,
    }
    return render(request, "game.html", context=context)

@login_required
def leaderboard(request):
    scores = models.Profile.objects.all()
    title = "Leaderboards"
    content = "Welcome to my work in progress!(leaderboard)"
    context = {
        "title":title,
        "body":content,
        "scores":sorted(scores, key=attrgetter('points'),reverse=True)
    }
    return render(request, "leaderboard.html", context=context)

@login_required
def chat(request):
    title = "Chat Rooms"
    content = "Welcome to my work in progress!(chat)"
    context = {
        "title":title,
        "body":content,
    }
    return render(request, "chat.html", context=context)
    
@login_required
def contact(request):

    if request.method == 'POST':
        message_name = request.POST['message-user-email']
        message_email = request.POST['message-user-email']
        message = request.POST['message']
        
        # send email
        send_mail(
            'Contact Attempt-'+ message_name, #subject
            message, #message
            message_email, # from email
            ['aragonderrick23@gmail.com'], # to email  
        )
         
        title = "Contact"
        context = {
            "title":title,
            "message_name": message_name,
        }
        return render(request, "contact.html", context=context)
    else:
        title = "Contact"
        context = {
            "title":title,
        }
        return render(request, "contact.html", context=context)

@login_required
def scoreSet(request, s):
    userProfile = models.Profile.objects.get(user=request.user)
    userProfile.points = userProfile.points + s
    userProfile.save()

    response_data = {'success':1}
    return HttpResponse(json.dumps(response_data), content_type="application/json")