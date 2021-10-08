from django.shortcuts import render
from django.views.generic import TemplateView
import pickle

# Create your views here.
# def Signup(request):
#     return render(request, 'signup.html')

# def Login(request):
#     return render(request, 'login.html')


class homepage(TemplateView):
    template_name = 'index.html'


def PCOD(request):
    return render(request, 'PCOD.html')



def result_PCOD(request):
    temp = {}
    temp['Q1'] = int(request.POST.get('Q1'))
    temp['Q2'] = int(request.POST.get('Q2'))
    temp['Q3'] = int(request.POST.get('Q3'))
    temp['Q4'] = int(request.POST.get('Q4'))
    temp['Q5'] = int(request.POST.get('Q5'))
    temp['Q6'] = int(request.POST.get('Q6'))
    temp['Q7'] = int(request.POST.get('Q7'))
    temp['Q8'] = int(request.POST.get('Q8'))
    temp['Q9'] = int(request.POST.get('Q9'))
    temp['Q10'] = int(request.POST.get('Q10'))
    temp['Q11'] = int(request.POST.get('Q11'))
    temp['Q12'] = int(request.POST.get('Q12'))
    temp['Q13'] = float(request.POST.get('Q13'))
    temp['Q14'] = float(request.POST.get('Q14'))
    temp['Q15'] = int(request.POST.get('Q15'))
    temp['Q16'] = int(request.POST.get('Q16'))
    temp['Q17'] = int(request.POST.get('Q17'))
    temp['Q18'] = int(request.POST.get('Q18'))
    temp['Q19'] = int(request.POST.get('Q19'))
    print(temp)
    input_list = list(temp.values())
    print(input_list)
    res = getPredictions(input_list)
    print(res)

    context = {
        'result': res
    }

    return render(request, 'result_PCOD.html', context)

def getPredictions(input_list):
    model = pickle.load(open('ML Models/PCOD_model.sav', 'rb'))

    prediction = model.predict(input_list)

    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'