from django.urls import path
from . import views
urlpatterns = [path('', views.index, name='index'),
path("AboutMe", views.AboutMe, name="AboutMe"),
path("login", views.login,name="login"),
path("JavaScript",views.JavaScript,name="JavaScript"),
path("gallery",views.gallery,name="gallery"),
path("contact",views.contact,name="contact")
]

