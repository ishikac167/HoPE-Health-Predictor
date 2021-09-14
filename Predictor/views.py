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

def getPredictions(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19):
    model = pickle.load(open('ml_model.sav', 'rb'))

    prediction = model.predict([
        [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19]
    ])
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result_PCOD(request):
    temp = {}
    temp['Q1'] = request.POST.get('gender')
    temp['Q2'] = request.POST.get('Q2')
    temp['Q3'] = request.POST.get('Q3')
    temp['Q4'] = request.POST.get('Q4')
    temp['Q5'] = request.POST.get('Q5')
    temp['Q6'] = request.POST.get('Q6')
    temp['Q7'] = request.POST.get('Q7')
    temp['Q8'] = request.POST.get('Q8')
    temp['Q9'] = request.POST.get('Q9')
    temp['Q10'] = request.POST.get('Q10')
    temp['Q11'] = request.POST.get('Q11')
    temp['Q12'] = request.POST.get('Q12')
    temp['Q13'] = request.POST.get('Q13')
    temp['Q14'] = request.POST.get('Q14')
    temp['Q15'] = request.POST.get('Q15')
    temp['Q16'] = request.POST.get('Q16')
    temp['Q17'] = request.POST.get('Q17')
    temp['Q18'] = request.POST.get('Q18')
    temp['Q19'] = request.POST.get('Q19')
    print(temp)
    input_list = list(temp.values())
    res = getPredictions(input_list)
    print(res)

    context = {
        'result': res
    }

    return render(request, 'result_PCOD.html', context)