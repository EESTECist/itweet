from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'maki1'

urlpatterns = [
   path('', PostListView.as_view(), ), 

]
