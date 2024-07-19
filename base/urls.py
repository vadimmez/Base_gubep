from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    # path("send", views.send, name="send"),
    path("form_conf", views.index2, name="form_conf"),
    path("done", views.done, name="done"),
    path("subscription", views.subscription, name="subscription"),


]

