from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import PostModel

# CRUD 

# Create

# Retrieve

# Update

# Delete

# List


def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    #return HttpResponse("some data")
    template = "blog/list-view.html"
    context = {
        "object_list": qs,
        #"some_dict": {"abc": 123},
        #"num": 123,
        #"array_list": [123, 423],
        #"boolean_value": True,

    }
    return render(request, template, context)

