from django.conf.urls import url

from .views import event_create, event_list


urlpatterns = [
    url(r'^new/', event_create, name='create'),
    url(r'^list/', event_list, name='list' ),
url(r'^list/', event_list, name='list' ),
]
