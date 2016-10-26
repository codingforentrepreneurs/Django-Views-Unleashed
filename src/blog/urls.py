from django.conf.urls import url


from .views import post_model_list_view

urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', home, name='home'),
    #url(r'^redirect/$', redirect_somewhere, name='home')
]
