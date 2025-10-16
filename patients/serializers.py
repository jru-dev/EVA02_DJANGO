from rest_framework import serializers
from .models import Doctor, Paciente

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'nombre', 'especialidad']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'edad', 'diagnostico', 'doctor']

class PacienteDetailSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'edad', 'diagnostico', 'doctor']

class DoctorDetailSerializer(serializers.ModelSerializer):
    pacientes = PacienteSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'nombre', 'especialidad', 'pacientes']
