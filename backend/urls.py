
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("api/search", include("search.urls")),
    path("api/products/", include("product.urls")),
    path("api/v2/", include("backend.routers")),
]
