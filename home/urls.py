from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('facility/<int:id>/', views.facility_detail, name='facility_detail'),
    path('about/', views.about, name='about'),
    path('academics/', views.Academics, name='academics'),
    path('admission/', views.Admission, name='admission'),
    path('program/', views.Program, name='program'),
    path('deafbind/', views.Deafblind, name='deafbind'),
]
