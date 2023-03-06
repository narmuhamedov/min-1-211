from django.urls import path
from . import views

urlpatterns = [
    #path('tvshow/', views.tvshow_view, name='show'),
    path('tvshow/', views.TvShowView.as_view(), name='show'),

    #path('tvshow/<int:id>/', views.tvshow_detail_view, name='show_detail'),
    path('tvshow/<int:id>/', views.TvShowDetailView.as_view(), name='show_detail'),
    #path('tvshow/<int:id>/update/', views.update_tv_show, name='update'),
    path('tvshow/<int:id>/update/', views.TvShowUpdateView.as_view(), name='update'),

    # path('tvshow/<int:id>/delete/',
    #      views.delete_tv_show, name='delete'),
    path('tvshow/<int:id>/delete/', views.TvShowDeleteView.as_view(), name='delete'),
    #path('add-show/', views.add_tv_show_view, name='add'),
    path('add-show/', views.TvShowCreateView.as_view(), name='add'),

]