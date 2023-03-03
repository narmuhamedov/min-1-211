from django.urls import path
from . import views

urlpatterns = [
    path('tvshow/', views.tvshow_view, name='show'),
    path('tvshow/<int:id>/', views.tvshow_detail_view, name='show_detail'),
    path('tvshow/<int:id>/update/', views.update_tv_show, name='update'),
    path('tvshow/<int:id>/delete/',
         views.delete_tv_show, name='delete'),
    path('add-show/', views.add_tv_show_view, name='add'),
]