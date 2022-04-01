from django.db import models

# Create your models here.
class Sede(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Ingrese nombre de la Sede",unique=True,error_messages={'unique':'Ya se encuentra Registrada'})
	direccion = models.CharField(max_length=100,verbose_name="Ingrese direccion")
	telefono = models.CharField(max_length=10,verbose_name="Ingrese Telefono de contacto")
	correo = models.EmailField(max_length=100,verbose_name="Digite correo electronico de contacto")
	timestamps = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Sede"
		verbose_name_plural = "Sedes"

	def __str__(self):
		return '%s'%(self.nombre)


class Curso(models.Model):
	curso = models.IntegerField(verbose_name="Ingrese grado",primary_key=True)
	sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
	timestamps = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s'%(self.curso)
    