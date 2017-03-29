from django.contrib import admin
from .models import Pedido, Especialidad, Articulo, Encargado, Pedido_Extra
from django_csv_exports.admin import CSVExportAdmin


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_entrega', 'fecha_pedido', 'cantidad', 'estado', 'articulo_id', 'especialidad', )
    list_filter = ('fecha_pedido', 'fecha_entrega', 'estado', 'especialidad',)
    search_fields = ('especialidad__nombre', 'articulo__nombre',)
    list_editable = ('especialidad','fecha_entrega',)



class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('cod_experto', 'nombre', 'descripcion', 'stock', 'extmin','extmax','info_bodega_id','total_pedido',)
    list_filter = ('cod_experto','info_bodega_id','total_pedido')
    search_fields = ('nombre','info_bodega_id__nombre',)
    list_display_links = ('cod_experto',)
    list_editable = ('nombre', 'descripcion','stock','extmin', 'extmax',)


class EspecialidadAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'estadistica', 'encargado',)
    list_filter   = ('nombre', 'encargado',)
    list_display_links = ('nombre','encargado',)
    list_editable = ('estadistica',)

class EncargadoAdmin(admin.ModelAdmin):
    list_display  = ('rut_encargado', 'nombre', 'usuario',)
    list_filter   = ('rut_encargado', 'nombre',)
    list_display_links = ('rut_encargado','usuario',)
    list_editable = ('nombre',)

class PedidoExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'articulo_ex', 'cantidad_ex', 'especialidad_ex', 'fecha_pedido_ex', 'fecha_entrega_ex', 'estado_ex',)
    list_filter =  ('articulo_ex', 'especialidad_ex', 'fecha_pedido_ex', 'fecha_entrega_ex', 'estado_ex',)
    search_fields = ('articulo_ex__nombre', 'especialidad_ex__nombre', 'estado_ex',)
    list_display_links = ('articulo_ex', 'especialidad_ex',)
    list_editable    = ('cantidad_ex', 'fecha_entrega_ex', )



admin.site.register(Pedido_Extra, PedidoExtraAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)


class ClientAdmin(CSVExportAdmin):
    pass 


