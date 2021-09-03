from django.shortcuts import render
from django.views.generic import TemplateView
import pickle


# Create your views here.
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
    Q1 = float(request.GET['Q1'])
    Q2 = float(request.GET['Q2'])
    Q3 = float(request.GET['Q3'])
    Q4 = float(request.GET['Q4'])
    Q5 = float(request.GET['Q5'])
    Q6 = float(request.GET['Q6'])
    Q7 = float(request.GET['Q7'])
    Q8 = float(request.GET['Q8'])
    Q9 = float(request.GET['Q9'])
    Q10 = float(request.GET['Q10'])
    Q11 = float(request.GET['Q11'])
    Q12 = float(request.GET['Q12'])
    Q13 = float(request.GET['Q13'])
    Q14= float(request.GET['Q14'])
    Q15 = float(request.GET['Q15'])
    Q16 = float(request.GET['Q16'])
    Q17 = float(request.GET['Q17'])
    Q18 = float(request.GET['Q18'])
    Q19 = float(request.POST.GET['Q19'])

    result_PCOD = getPredictions(Q1, Q2, Q3, Q4,
                            Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19)

    return render(request, 'result_PCOD.html', {'result_PCOD': result_PCOD})