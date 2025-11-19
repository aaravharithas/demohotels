"""
URL configuration for demorestjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from hotels.views import TodoVeiw, HotelsView,home,HotelDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home,name='home'),
    path("tasks/", TodoVeiw.as_view(), name='todoview'),
    # path("hotels/", HotelsView.as_view(), name='hotels'),
    path('hotels/', HotelsView.as_view(), name='hotels-list'),
    path('hotels/<int:id>/', HotelDetailView.as_view(), name='hotel-detail'),

]
