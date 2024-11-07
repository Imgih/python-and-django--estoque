from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Estoque
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def atualizar_estoque(request, produto_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        estoque_item, created = Estoque.objects.update_or_create(
            produto_id=produto_id,
            defaults={'quantidade': data['quantidade']}
        )
        return JsonResponse({
            'produto_id': estoque_item.produto_id,
            'quantidade': estoque_item.quantidade,
        })

@csrf_exempt
def remover_estoque(request, produto_id):
    if request.method == 'DELETE':
        estoque_item = get_object_or_404(Estoque, produto_id=produto_id)
        estoque_item.delete()
        return JsonResponse({'status': 'Produto removido do estoque'}, status=204)
