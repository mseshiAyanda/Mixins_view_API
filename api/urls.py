from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleMixinView.as_view()),
    path('<int:pk>/', views.article_mixin_view),
]