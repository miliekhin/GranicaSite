from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from kppshka import views

urlpatterns = [
    path('kpp/', views.KppInfo.as_view()),
    path('comments/', views.Comments.as_view()),
    path('telega_parser/', views.Telega.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
