from django.contrib import admin
from django.urls import path, include
# from blogs.views import BlogViewset
# from rest_framework.routers import DefaultRouter 


# router = DefaultRouter()

# router.register("", BlogViewset, basename = "blogs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blogs.urls")),
    path("auth/", include("accounts.urls"))
]
