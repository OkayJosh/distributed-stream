from django.urls import path, include
from websocket.urls import websocket
from . import views



urlpatterns = [
    path("", views.IndexView.as_view()),
    path( "api/", include('price.api.urls')),
    websocket("price/", views.websocket_view),
]
