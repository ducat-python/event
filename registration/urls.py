from django.conf.urls import url

from .views import register_new

urlpatterns = [
    url(r'^new/', register_new, name='new'),

]
