from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),


    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>/update', views.update, name='update'),
    path('<int:article_id>/like', views.like, name='like'),
    path('api/articles/<int:article_id>/like', views.api_like),
]