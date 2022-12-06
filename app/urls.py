from django.urls import path
from .views import index, decrease_counter, show_card

urlpatterns = [
    path('', index),
    path('c/', decrease_counter, name="c"),
    path("card/<code>/", show_card, name="show_card"),
]