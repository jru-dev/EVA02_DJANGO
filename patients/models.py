from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    specialty = models.CharField(max_length=255, verbose_name="Especialidad")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.specialty}"

class Patient(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    age = models.IntegerField(verbose_name="Edad")
    diagnosis = models.TextField(verbose_name="Diagnóstico")
    doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE, verbose_name="Doctor asignado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.age} años)"