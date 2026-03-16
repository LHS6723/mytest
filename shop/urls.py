from django.urls import path
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('detail/<int:id>',views.detail,name='detail'),
        path('about/',views.about,name='about'),
        path('service/',views.service,name='service'),
        path('contact/',views.contact,name='contact'),
        path('team/',views.team,name='team'),
        ]