"""
URL configuration for votingproject project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('amin/', admin.site.urls),
    path("demo", views.demofunctio, name="demo"),
    path("", views.homefunction, name="home"),
    path("voterregistration", views.voterregistratiofunction, name="voterregistration"),
    path('createregister/', views.createregister, name ='crateregister'),
    path("result", views.resultsfunction, name="result"),
    path("candidateinformation", views.candidateinformationfunction, name="candidateinformation"),
    path("complaint", views.complaintfunction, name="complaint"),
    path("login", views.login, name="login"),
    path("checkaminlogin", views.checkaminlogin, name="checkaminlogin"),
    path("voting", views.voting, name="voting"),
    path("signup", views.singup, name="signup"),
    path('createuser/', views.createuser, name='createuser'),
    path("", include("aminapp.urls")),

    # path("",include("voterapp.urls")),
]
