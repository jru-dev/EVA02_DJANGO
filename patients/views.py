from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Doctor, Paciente
from .serializers import (
    DoctorSerializer, DoctorDetailSerializer,
    PacienteSerializer, PacienteDetailSerializer
)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return DoctorDetailSerializer
        return DoctorSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.select_related('doctor').all()
    serializer_class = PacienteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre', 'diagnostico']
    filterset_fields = ['doctor']

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return PacienteDetailSerializer
        return PacienteSerializer
