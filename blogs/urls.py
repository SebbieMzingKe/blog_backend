from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name = "posts_home"),
    path("", views.BlogListCreateView.as_view(), name = "list_blogs"),
    path("<int:pk>", views.BlogRetrieveUpdateDeleteView.as_view(), name = "blog_detail"), 
]