# from . import views


 

# urlpatterns = [

#     # path("homepage/", views.homepage, name = "posts_home"),
#     # path("", views.BlogListCreateView.as_view(), name = "list_blogs"),
#     # path("<int:pk>", views.BlogRetrieveUpdateDeleteView.as_view(), name = "blog_detail"), 
# ]

from django.contrib import admin
from django.urls import path, include
from blogs.views import BlogViewset
from rest_framework.routers import DefaultRouter 


router = DefaultRouter()

router.register("", BlogViewset, basename = "blogs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blogs/", include(router.urls))
]
