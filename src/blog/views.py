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
    context = {}
    return render(request, template, context)

