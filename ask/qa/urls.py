
from qa.views import test
# from django.contrib import url
# from django.urls import path, url
from django.conf.urls import url as path

print('fuck!')

urlpatterns = [
    path(r'.*', test, name='home'),
    #url(r'^question/(\d+)/*', test, name='question'),
    #url(r'^login/*', test, name='login'),
    #url(r'^signup/*', test, name='signup'),
    #url(r'^ask/*', test, name='ask'),
    #url(r'^popular/*$', test, name='popular'),
    #url(r'^new/*$', test, name='new'),
]
