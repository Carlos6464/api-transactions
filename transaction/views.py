from django.http import JsonResponse

def transactions(request):
    if request.method == 'GET':
        data = {
            'transactions': [
                {'id': 1, 'amount': 100.00, 'currency': 'USD'},
                {'id': 2, 'amount': 200.00, 'currency': 'EUR'},
            ]
        }
        return JsonResponse(data)
