from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .forms import PostModelForm
from .models import PostModel

#@login_required
def post_model_create_view(request):
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Created a new blog post!")
        context = {
            "form": PostModelForm()
        }
        #return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    
    template = "blog/create-view.html"
    return render(request, template, context)

#@login_required
def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    
    template = "blog/update-view.html"
    return render(request, template, context)


def post_model_detail_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)



def post_model_delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Post deleted")
        return HttpResponseRedirect("/blog/")
    context = {
        "object": obj,
    }
    template = "blog/delete-view.html"
    return render(request, template, context)


def post_model_list_view(request):
    #query = request.GET["q"]
    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(slug__icontains=query)
                )
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




def post_model_robust_view(request, id=None):
    obj = None
    context =  {}
    success_message = 'A new post was created'
    
    if id is None:
        "obj is could be created"
        template = "blog/create-view.html"
    else:
        "obj prob exists"
        obj = get_object_or_404(PostModel, id=id)
        success_message = 'A new post was created'
        context["object"] = obj
        template = "blog/detail-view.html"
        if "edit" in request.get_full_path():
            template = "blog/update-view.html"
        if "delete" in request.get_full_path():
            template = "blog/delete-view.html"
            if request.method == "POST":
                obj.delete()
                messages.success(request, "Post deleted")
                return HttpResponseRedirect("/blog/")

    #if "edit" in request.get_full_path() or "create" in request.get_full_path():
    form = PostModelForm(request.POST or None, instance=obj)
    context["form"] = form
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, success_message)
        if obj is not None:
            return HttpResponseRedirect("/blog/{num}".format(obj.id))
        context["form"] - PostModelForm()
    return render(request, template, context)







