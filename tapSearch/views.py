from django.shortcuts import render

def index(request):


    context_dict={
        "name": "gurtej"
    }
    return render(request, "tapSearch/index.html", context=context_dict)
