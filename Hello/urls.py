'''URLs (URL Patterns):
URLs, also known as URL patterns, define the mapping between URLs entered by users in their web browsers and the corresponding views that should be invoked to handle those URLs. URL patterns are defined in the Django project's urls.py module.
In the urls.py file, you specify regular expressions or simple strings to match specific URLs and associate them with the corresponding view functions. Django will compare the requested URL against the defined URL patterns and execute the view associated with the first pattern that matches the request.'''



"""
URL configuration for Hello project.

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
from . import views

# Basic code for learning django views concept?

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", views.index , name = "index"),
#     path("about/" , views.about , name = "about"), # first argument is path , second is function and third is name 
#     # agr path hamara lengthy ho ya complex hoto hm nam se bh access kr skte hn  jo hm template wagera m dekhenge
#     path("home/" , views.home , name = "home"),
    
#     path("navigator page" , views.navigatorpage , name = "navigator page")
# ]
      

# Code for pipeline:

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", views.index , name = "index"),
#     path("removpunc" , views.removepunc , name = "rempunc"), 
#     path("capitalizefirst" , views.capfirst , name = "capfirst"),
#     path("spaceremove" , views.spaceremove , name = "spaceremove"),
#     path("charcount" , views.charcount , name = "charcount"),

    #   ]


#  code for understanding template:
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", views.index , name = "index"),
#     path('removepunc', views.removepunc , name = 'removepunc'),

# ]

# Code for Backend Concept
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index , name = "index"),
    path('analyze', views.analyze , name = 'analyze'),

]
