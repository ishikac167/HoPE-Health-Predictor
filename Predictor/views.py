from django.shortcuts import render
from django.views.generic import TemplateView
import pickle
from bs4 import BeautifulSoup
import requests

# Create your views here.
# def Signup(request):
#     return render(request, 'signup.html')

# def Login(request):
#     return render(request, 'login.html')


class homepage(TemplateView):
    template_name = 'index.html'


def PCOD(request):
    return render(request, 'PCOD.html')

def getPredictions(input_list):
    model = pickle.load(open('ML Models/PCOD_model.sav', 'rb'))

    prediction = model.predict(input_list)

    if prediction == 1:
        return 'yes'
    elif prediction == 0:
        return 'no'
    else:
        return 'error'

def result_PCOD(request):
    temp = {}
    temp['Q1'] = request.POST.get('Q1')
    temp['Q2'] = int(request.POST.get('Q2'))
    temp['Q3'] = int(request.POST.get('Q3'))
    temp['Q4'] = int(request.POST.get('Q4'))
    temp['Q5'] = int(request.POST.get('Q5'))
    temp['Q6'] = int(request.POST.get('Q6'))
    temp['Q7'] = int(request.POST.get('Q7'))
    temp['Q8'] = int(request.POST.get('Q8'))
    temp['Q9'] = int(request.POST.get('Q9'))
    temp['Q10'] = int(request.POST.get('Q10'))
    temp['Q11'] = request.POST.get('Q11')
    temp['Q12'] = int(request.POST.get('Q12'))
    temp['Q13'] = float(request.POST.get('Q13'))
    temp['Q14'] = float(request.POST.get('Q14'))
    temp['Q15'] = int(request.POST.get('Q15'))
    temp['Q16'] = int(request.POST.get('Q16'))
    temp['Q17'] = int(request.POST.get('Q17'))
    temp['Q18'] = int(request.POST.get('Q18'))
    temp['Q19'] = request.POST.get('Q19')
    print(temp)
    input_list = list(temp.values())
    print(input_list)
    res = getPredictions(input_list)
    print(res)

    context = {
        'result': res
    }

    return render(request, 'result_PCOD.html', context)

def DocInput(request):
    return render(request,'doctor_input.html')

def DocRecomm(request):
    if request.method == 'POST':
        temp={}
        temp['specialist'] = request.POST.get('specialist')
        temp['city'] = request.POST.get('city')
        city = temp['city']
        specialist = temp['specialist']
        error = False
        data = []
        try:
            url = 'https://www.practo.com/'+city+'/'+specialist
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text,'lxml')
            names = soup.find_all('h2',class_='doctor-name')
            places = soup.find_all('div',class_='u-bold u-d-inlineblock u-valign--middle')
            for i in range(len(names)):
                val = {'name':names[i].text,'place':places[i].text}
                data.append(val)
        except:
            error = True
        return render(request,'doctor.html', {'data':data})