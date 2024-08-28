import requests
from rest_framework import views
from rest_framework.response import Response

class PurchaseProductView(views.APIView):

    def post(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        quantity = request.data['quantity']


    #TODO 1. Verificar disponibilidade do estoque no Inventory Service



    #2. Criar o pedido no Product Service

        order_response = requests.post('http://localhost:8001/api/orders/', json={
            'product_id': product_id,
            'quantity': quantity
        })
        
        if order_response.status_code != 200:
            return Response({'error': 'Failed to create order'}, status=400)

        order_id = order_response.json().get('order_id')


    # 3. Reservar o pedido no Inventory Service

        inventory_reserve_response = requests.post('http://localhost:8002/api/inventory/reserve/', json={
                'product_id': product_id,
                'quantity': quantity
            })

        if inventory_reserve_response.status_code != 200:
            return Response({'error': 'Failed to reserve inventory'}, status=400)



    #TODO 4. Processar o pagamento no Payment Service
        

        
        