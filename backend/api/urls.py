from django.urls import path

from api import views

# urlpatterns = [
#
#     path('<str:url1>/<str:url2>/<str:url3>/<str:url4>/<str:url5>/<str:url6>', views.get_data),
#
# ]

urlpatterns = [

    path("add/", views.get_data),

]
