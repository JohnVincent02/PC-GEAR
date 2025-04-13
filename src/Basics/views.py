#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def calculator(request):
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # Evaluate the expression securely
            result = eval(expression)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render(request, 'Basics/calculator.html', {'result': result})

