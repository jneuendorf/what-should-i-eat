"""what_should_i_eat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns = [
    # # tinymce
    # url(r'^tinymce/', include('tinymce.urls')),
    # landing page
    url(r'^$', views.index, name='index'),
    url(r'^cook_recipe/(?P<recipe_id>[0-9]+)/$', views.cook_recipe, name='cook_recipe'),
    url(r'^dismiss_recipe/(?P<recipe_id>[0-9]+)/$', views.dismiss_recipe, name='dismiss_recipe'),
    url(r'^recipe_overview/(?P<recipe_id>[0-9]+)/$', views.recipe_overview, name='recipe_overview'),
    # recipe book
    url(r'^recipe-book/', include('recipe_book.urls')),
    # admin
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
