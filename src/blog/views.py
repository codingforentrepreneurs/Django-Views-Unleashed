from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import PostModel

# CRUD 

# Create

# Retrieve

# Update

# Delete

# List

def post_model_detail_view(request, id=None):
    #print(id)
    # try:
    #     obj = PostModel.objects.get(id=100)
    # except:
    #     raise Http404
    # qs = PostModel.objects.filter(id=100)
    # obj = None
    # if not qs.exists() and qs.count() !=1:
    #     raise Http404
    # else:
    #     obj = qs.first()

    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


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

