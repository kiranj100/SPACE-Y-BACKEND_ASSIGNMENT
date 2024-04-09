from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Shopping Mall API",
      default_version='v1',
      description="API for managing products, customers, and bills in a shopping mall",
      terms_of_service="https://www.example.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('billing_app.urls')),
    path('', lambda request: redirect('schema-swagger-ui', permanent=False)),  # Redirect root URL to Swagger UI URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
