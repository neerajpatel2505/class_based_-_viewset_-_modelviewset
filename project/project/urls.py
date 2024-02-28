"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from app.views import List, Details
from app.views import StudentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("studentapi",StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('list/',List.as_view()),
    # path('details/<int:pk>',Details.as_view()),
    path('',include(router.urls))
]

