from django.contrib import admin
from django.urls import path
from .views import home,upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path("upload/", upload_image),

]
