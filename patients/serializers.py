from rest_framework import serializers
from .models import Patient, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'created_at', 'updated_at']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'diagnosis', 'doctor', 'created_at', 'updated_at']