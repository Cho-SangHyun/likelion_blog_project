"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog import views
from portfolio import views as pf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about_me/', views.intro, name="intro"),
    path('blog/', views.blog, name="blog"),
    path('blog/<int:blog_id>', views.detail, name="detail"),
    path('blog/new/', views.new, name="new"),
    path('blog/new/create', views.create, name="create"),
    path('blog/<int:blog_id>/delete', views.delete, name="delete"),
    path('blog/<int:blog_id>/edit', views.edit, name="edit"),
    path('blog/<int:blog_id>/update', views.update, name="update"),
    path('portfolio/', pf.portfolio, name="portfolio"),
]
