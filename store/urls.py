from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^store/', views.listing, name="store.listing"),
]
