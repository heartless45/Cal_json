from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def hello(request):
    return JsonResponse({'message':'Helloworld'})

def cal(request):
    num1 = float(request.GET.get('num1',0))
    num2 = float(request.GET.get('num2', 0))
    op = request.GET.get('op','')

    result = None

    if op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1 * num2
    elif op == 'div':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return JsonResponse({'error':'division error'})

    if result is not None:
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Invalid'})

