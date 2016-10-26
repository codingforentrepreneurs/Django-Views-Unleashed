from django.http import HttpResponse, HttpResponseRedirect


# Class Home

# def home(request):
#     print(request)
#     print(dir(request))
#     #print(request.method)
#     #print(request.is_ajax)
#     #print(request.is_ajax())
#     print(request.get_full_path())
#     return HttpResponse("<!DOCTYPE html><html><head><style>h1{color: red;}</style></head><body><h1>Hello World</h1></body></html>")


def home(request):
    # save data

    response = HttpResponse(content_type='application/json')
    response = HttpResponse(content_type='text/html')
   
    response.content = '<!DOCTYPE html><html><head><style>h1{color: red;}</style></head><body><h1>Hello World</h1></body></html>'
    print(response.status_code)
    print(dir(response))
    #response.write("<p>Page Not Found</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    response.status_code = 200
    return response


def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path") # http://joincfe.com
