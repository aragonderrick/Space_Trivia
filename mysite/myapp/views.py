from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            suggestion_form = forms.SuggestionForm()
            return HttpResponseRedirect('0')
    else:
        suggestion_form = forms.SuggestionForm()
    suggestions = models.suggestionModel.objects.all()
    context = {
        "title":"suggestions",
        "suggestions":suggestions,
        "form":suggestion_form,
    }
    return render(request, "index.html", context=context)

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

    title = "KnowUrPlanet"
    content = "Welcome to my work in progress! CINS465 Hello World!"
    context = {
        "title":title,
        "body":content,
        "card":card,
        "prev":page-1,
        "next":page+1
    }
    return render(request, "page.html", context=context)