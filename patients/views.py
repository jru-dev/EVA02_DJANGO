from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Patient, Doctor
from .serializers import PatientSerializer, PatientDetailSerializer, DoctorSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': 'HealthTrack API v1 - Gestor de Pacientes',
        'endpoints': {
            'patients': reverse('patient-list', request=request, format=format),
            'doctors': reverse('doctor-list', request=request, format=format),
        }
    })

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'diagnosis']
    filterset_fields = ['doctor__specialty', 'age']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PatientDetailSerializer
        return PatientSerializer
    
    def get_queryset(self):
        queryset = Patient.objects.all()
        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            queryset = queryset.filter(
                models.Q(name__icontains=search_query) |
                models.Q(diagnosis__icontains=search_query) |
                models.Q(doctor__name__icontains=search_query) |
                models.Q(doctor__specialty__icontains=search_query)
            )
        return queryset

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'specialty']