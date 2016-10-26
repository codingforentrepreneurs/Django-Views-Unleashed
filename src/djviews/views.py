from django.http import HttpResponse


# Class Home

def home(request):
    #print(request)
    print(dir(request))
    #print(request.method)
    #print(request.is_ajax)
    #print(request.is_ajax())
    print(request.get_full_path())
    return HttpResponse("<!DOCTYPE html><html><head><style>h1{color: red;}</style></head><body><h1>Hello World</h1></body></html>")