from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    context = {
        "object_list": qs,
    }
    template = "blog/list-view.html"
    return render(request, template, context)



@login_required(login_url='/login/')
def login_required_view(request):
    print(request.user)
    qs = PostModel.objects.all()
    context = {
        "object_list": qs,
    }

    if request.user.is_authenticated():
        template = "blog/list-view.html"
    else:
        template = "blog/list-view-public.html"
        #raise Http404
        return HttpResponseRedirect("/login")
    
    return render(request, template, context)

