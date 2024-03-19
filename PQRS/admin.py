from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PQRS,PQRSRespuesta
from django.db.models.signals import post_save
from django.dispatch import receiver


@admin.register(PQRS)
class PQRSAdmin(ImportExportModelAdmin):
    list_display = ('tipoPQRS', 'fechaPQRS', 'cliente','DescripcionPQRS','EstadoPQRS')
    #list_display_links = ('name')
    list_editable = ('EstadoPQRS',)
    search_fields = ('DescripcionPQRS',)
    list_filter = ('EstadoPQRS','fechaPQRS','tipoPQRS',)
    list_per_page = 5

    @receiver(post_save, sender=PQRSRespuesta)
    def actualizar_estado_pqrs(sender, instance, created, **kwargs):
        if created:
            # Obtén la PQRS asociada a esta respuesta
            pqrs = instance.pqrs
            # Actualiza el estado de la PQRS del cliente con el estado de la respuesta
            pqrs.EstadoPQRS = instance.estado
            pqrs.save()

@admin.register(PQRSRespuesta)
class PQRSRespuestaAdmin(ImportExportModelAdmin):
    list_display = ('pqrs', 'estado', 'respuesta','fecha_respuesta','User')
    #list_display_links = ('name')
    list_editable = ('estado',)
    search_fields = ('respuesta',)
    list_filter = ('estado','fecha_respuesta','pqrs',)
    list_per_page = 5

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "User":
            # Establece el valor del campo "User" en el usuario autenticado
            kwargs["initial"] = request.user.id
            return db_field.formfield(**kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)