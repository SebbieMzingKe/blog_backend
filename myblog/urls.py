from django.contrib import admin
from django.urls import path, include, re_path
# from blogs.views import BlogViewset
# from rest_framework.routers import DefaultRouter 


# router = DefaultRouter()

# router.register("", BlogViewset, basename = "blogs")

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="This is an API for a Blogging Application",
      # terms_of_service="https://www.google.com/policies/terms/",
      # contact=openapi.Contact(email="contact@snippets.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   re_path('swagger<format>/', 
    schema_view.without_ui(cache_timeout=0),
    name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("auth/", include("accounts.urls"))
]
