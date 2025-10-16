from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200, default="General") 

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.PositiveIntegerField(default=0)  
    diagnostico = models.TextField(blank=True, default="Sin diagnóstico") 
    doctor = models.ForeignKey(
        Doctor,
        related_name='pacientes',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nombre} - {self.diagnostico[:30]}"
