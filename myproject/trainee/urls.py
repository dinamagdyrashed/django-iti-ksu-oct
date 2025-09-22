from django.urls import path
from .views import *
urlpatterns = [
    path('',alltrainee),
    path('traineeid/',gettraineeid),
    path('Insert/',inserttrainee),
    path('Update/<int:id>',updatetrainee,name='updatetrainee'),
    path('Dalete/<int:id>',deletetrainee,name='deletetrainee'),
]