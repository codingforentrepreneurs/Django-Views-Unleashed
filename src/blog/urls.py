from django.conf.urls import url


from .views import (
    post_model_detail_view,
    post_model_list_view
    )

urlpatterns = [
    url(r'^$', post_model_list_view, name='list'),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', home, name='home'),
    #url(r'^redirect/$', redirect_somewhere, name='home')
]
