from django.shortcuts import render
from django.views.generic import TemplateView
import pickle
from bs4 import BeautifulSoup
import requests
import cv2
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .main import Main
from .firebase import FirebaseClient
from firebase_admin import auth
#from rest_framework import viewsets, status
#from rest_framework.response import Response

# Create your views here.
# def Signup(request):
#     return render(request, 'signup.html')
fb_client = FirebaseClient()

user_details = {}


def Login(request):
    return render(request, 'login.html')


def loginuser(request):
    if request.method == "POST":
        user = auth.get_user_by_email(request.POST.get('email'))
        print(user.uid)
        global user_details
        user_details = fb_client.get_by_id(user.uid)
        print(user_details)
    return render(request, 'index.html', user_details)


def dashboard(request, user_id):
    print(user_id)
    user_details = fb_client.get_by_id(user_id)

    return render(request, 'dash.html', user_details)


def updateuser(request, user_id):
    print(user_id)
    user_details = fb_client.get_by_id(user_id)
    if request.method == "POST":
        data = {}
        data['name'] = request.POST.get('name')
        data['bloodgroup'] = request.POST.get('bloodgroup')
        data['dob'] = request.POST.get('dob')
        data['gender'] = request.POST.get('gender')
        data['weight'] = request.POST.get('weight')
        data['height'] = request.POST.get('height')
        fb_client.update(user_id, data)
    return render(request, "dash.html", user_details)


def signup(request):
    if request.method == "POST":
        data = {}
        data['name'] = request.POST.get('name')
        data['email'] = request.POST.get('sign-up-email')
        data['password'] = request.POST.get('sign-up-password')
        data['ailments'] = []
        data['bloodgroup'] = ""
        data['chd'] = []
        data['colorb'] = []
        data['dob'] = ''
        data['gender'] = ''
        data['lastTestTaken'] = ''
        data['myopia'] = []
        data['pcod'] = []
        data['urlAvatar'] = ''
        data['weight'] = ''

        user = auth.create_user(
            email=data['email'], password=data['password'], display_name=data['name'])

        fb_client.create(data, user.uid)
    return render(request, 'login.html')


baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL

with open(baseUrl + 'heart_attack_pred_model.pkl', 'rb') as file:
    cat_model = pickle.load(file)


def convert_time(time):
    h = int(time[:2])
    m = int(time[3:])
    return float(h + (m/60))


def predict_from_arr(arr):
    pred = cat_model.predict(arr)
    return(pred)

# Create your views here.


def HA(request):

    return render(request, 'HA.html')


def result_HA(request):
    if request.method == 'POST':
        temp = {}
        temp['gender'] = request.POST.get('gender')
        temp['age'] = request.POST.get('age')
        temp['currentSmoker'] = request.POST.get('currentSmoker')
        temp['cigsPerDay'] = request.POST.get('cigsPerDay')
        temp['BPMeds'] = request.POST.get('BPMeds')
        temp['prevalentStroke'] = request.POST.get('prevalentStroke')
        temp['prevalentHyp'] = request.POST.get('prevalentHyp')
        temp['diabetes'] = request.POST.get('diabetes')
        temp['totChol'] = request.POST.get('totChol')
        temp['sysBP'] = request.POST.get('sysBP')
        temp['diaBP'] = request.POST.get('diaBP')
        temp['bmi'] = request.POST.get('bmi')
        temp['glucose'] = request.POST.get('glucose')
        fileObj = request.FILES['video']
        print(temp)
        input_list = list(temp.values())
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name, fileObj)
        filePathName = fs.url(filePathName)
        print(filePathName)

        testVid = '.'+filePathName

        print(testVid)
        file = Main(testVid)
        bpm = round(file.capture_bpm())
        print(bpm)
        input_list.insert(-1, bpm)
        print(input_list)
        res = predict_from_arr(input_list)
        print(res)

        context = {
            'heartRate': bpm,
            'result': res
        }
    return render(request, 'result_HA.html', context)


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
    temp['Q13'] = convert_time(request.POST.get('Q13'))
    temp['Q14'] = convert_time(request.POST.get('Q14'))
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
    return render(request, 'doctor_input.html')


def DocRecomm(request):
    if request.method == 'POST':
        temp = {}
        temp['specialist'] = request.POST.get('specialist')
        temp['city'] = request.POST.get('city')
        city = temp['city']
        specialist = temp['specialist']
        error = False
        data = []
        try:
            url = 'https://www.practo.com/'+city+'/'+specialist
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'lxml')
            names = soup.find_all('h2', class_='doctor-name')
            places = soup.find_all(
                'div', class_='u-bold u-d-inlineblock u-valign--middle')
            for i in range(len(names)):
                val = {'SrNo': i+1,
                       'name': names[i].text, 'place': places[i].text}
                data.append(val)
        except:
            error = True
        return render(request, 'doctor.html', {'data': data})


def health_journal(request):
    return render(request, 'journal.html')
