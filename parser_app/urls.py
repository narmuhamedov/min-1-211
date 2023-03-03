from django.urls import path
from . import views

urlpatterns = [
    path('parser_film/', views.ParserFormView.as_view(), name='parser_form'),
    path('film_list/', views.FilmListView.as_view(), name='film_list'),
]