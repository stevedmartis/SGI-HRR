from django.http import JsonResponse

from .models import Pedido


def ingresar_cantidad(request, id_pedido):
    pk = request.POST.get('id_pedido')
    pedido = Pedido.objects.get(id=pk)
    pedido.save()
    response = {}
    return JsonResponse(response)