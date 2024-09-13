from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'), 
    path('about/',views.about, name='about'), 
    path('blogs/',views.blog, name='blog'), 
    path('services/',views.services, name='services'), 
    path('portfolio/',views.portfolio, name='portfolio'), 
    path('review/',views.review, name='review'), 
    path('form/',views.form, name='form'), 
    path('worker/',views.worker, name='worker'), 
]
