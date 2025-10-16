from rest_framework import serializers
from .models import Patient, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    patient_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'patient_count', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_patient_count(self, obj):
        return obj.patients.count()

class PatientSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    doctor_specialty = serializers.CharField(source='doctor.specialty', read_only=True)
    
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'diagnosis', 'doctor', 'doctor_name', 'doctor_specialty', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class PatientDetailSerializer(serializers.ModelSerializer):
    doctor_info = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'diagnosis', 'doctor', 'doctor_info', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']