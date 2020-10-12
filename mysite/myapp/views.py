from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

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
def page(request, page=0):
    card = []#list[]
    for i in range(1, 21):#generate 20 cards
        if i % 2 != 0:
            card_dict = {
                "cardTitle": "Saturn Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Saturn Card #" + str(i),
                "counter": i
            }
        else:
            card_dict = {
                "cardTitle": "Uranus Card #" + str(i),
                "subtitle": "Subtitle of Card #" + str(i),
                "info": "Info of Uranus Card #" + str(i),
                "counter": i 
            }
        card.append(card_dict)

    title = "Know Your Planet"
    content = "Welcome to my work in progress! CINS465 Hello World!"
    context = {
        "title":title,
        "body":content,
        "card":card,
        "prev":page-1,
        "next":page+1
    }
    return render(request, "page.html", context=context)

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