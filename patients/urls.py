from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PacienteViewSet

router = DefaultRouter()
router.register(r'doctores', DoctorViewSet, basename='doctores')
router.register(r'pacientes', PacienteViewSet, basename='pacientes')

urlpatterns = [
    path('', include(router.urls)),
]
