from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
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

    title = "CINS465"
    content = "Welcome to my work in progress! CINS465 Hello World!"
    context = {
        "title":title,
        "body":content,
        "card": card,
    }
    return render(request,"base.html", context=context)