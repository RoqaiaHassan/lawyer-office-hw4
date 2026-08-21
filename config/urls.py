from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.urls")),
    path("lawyer/", include("lawyer.urls")),
    path("store/", include("store.urls")),
]