from django.contrib import admin
from app.models import Palestra

admin.site.site_header = 'Jacitec2019'
admin.site.site_title = 'Jacitec2019'


@admin.register(Palestra)
class PalestraAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'data',
        'hora_inicio',
        'hora_fim',
        'palestrantes',
        'categoria',
        'vagas_total',
        'vagas_restantes',
        'local',
    )

    # filter_horizontal = (
    #    'categoria',
    # )


# admin.site.register(Palestra)
