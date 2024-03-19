from django.db import models
from Usuarios.models import Cliente,User

class PQRS(models.Model):
    # Definir las opciones para el campo tipo "select" de Tipo de PQRS
    OPCIONES_TIPO_PQRS = [
        ('Pregunta', 'Pregunta'),
        ('Queja', 'Queja'),
        ('Reclamo', 'Reclamo'),
        ('Sugerencia', 'Sugerencia'),
    ]

    # Campo CharField con choices para el Tipo de PQRS
    tipoPQRS = models.CharField(
        max_length=20,
        verbose_name='Tipo de PQRS',
        choices=OPCIONES_TIPO_PQRS,
    )

    # Definir las opciones para el campo tipo "select" de Estado de PQRS
    OPCIONES_ESTADO_PQRS = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    # Campo CharField con choices para el Estado de PQRS
    EstadoPQRS = models.CharField(
        max_length=20,
        verbose_name='Estado de PQRS',
        choices=OPCIONES_ESTADO_PQRS,
        default='Pendiente',  # Puedes establecer un valor predeterminado si lo deseas
    )

    # Resto de tus campos
    fechaPQRS = models.DateField(verbose_name='Fecha de PQRS')
    DescripcionPQRS = models.TextField(max_length=100, verbose_name='Descripción de PQRS')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')

    def __str__(self):
        return self.tipoPQRS

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRSs'
        db_table = 'pqrs'
        ordering = ['tipoPQRS']

class PQRSRespuesta(models.Model):
    respuesta = models.TextField(max_length=100, verbose_name='Respuesta')
    
    # Definir las opciones para el campo "select" de Estado de respuesta de PQRS
    OPCIONES_ESTADO_RESPUESTA = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    estado = models.CharField(
        max_length=20,
        verbose_name='Estado de respuesta',
        choices=OPCIONES_ESTADO_RESPUESTA,  # Usar las opciones definidas arriba
    )

    fecha_respuesta = models.DateField(verbose_name='Fecha de respuesta')
    pqrs = models.ForeignKey(PQRS, on_delete=models.CASCADE, verbose_name='PQRS')
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.respuesta

    class Meta:
        verbose_name = 'Respuesta de PQRS'
        verbose_name_plural = 'Respuestas de PQRS'
        db_table = 'pqrs_respuesta'
        ordering = ['respuesta']