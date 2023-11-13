from django.urls import path

from guestapp.views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleListView, test
from homeapp.views import index, introduce, team

app_name='guestapp'

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('list/', ArticleListView.as_view(), name='list'),
    path('test/', test, name='test'),

]