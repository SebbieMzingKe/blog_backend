from . import views
from django.urls import path


 

urlpatterns = [

    path("homepage/", views.homepage, name = "blogs_home"),
    path("", views.BlogListCreateView.as_view(), name = "list_blogs"),
    path("<int:pk>", views.BlogRetrieveUpdateDeleteView.as_view(), name = "blog_detail"), 
    path("current_user/", views.get_blog_for_current_user, name = "current_user"),
    path("blogs_for/", views.ListBlogForAuthor.as_view(), name = "blog_for_current_user")

]

# from django.contrib import admin
# from django.urls import path, include
# from blogs.views import BlogViewset
# from rest_framework.routers import DefaultRouter 
# from . import views


# router = DefaultRouter()

# router.register("", BlogViewset, basename = "blogs")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("blogs/", include(router.urls)),
#     path("current_user/", views.get_blog_for_current_user, name = "current_user")
# ]
