from django.shortcuts import render

def PCOD(request):
    return render(request, 'PCOD.html')

def result_PCOD(request):
    return render(request, 'result_PCOD.html')