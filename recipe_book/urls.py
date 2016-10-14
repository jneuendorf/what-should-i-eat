from django.conf.urls import url
from . import views

app_name = 'recipe_book'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^add/$', views.add, name='add'),
    url(r'^tags/$', views.tags, name='tags'),
]
