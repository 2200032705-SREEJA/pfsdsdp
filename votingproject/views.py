from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect



from aminapp.models import  signup  , createregister


def demofunctio(request):
    return render(request, "main.html")


def homefunction(request):
    return render(request, "index.html")


def voterregistratiofunction(request):
    return render(request, "voterregistratio.html")


def resultsfunction(request):
    return render(request, "results.html")


def candidateinformationfunction(request):
    return render(request, "candidateinformation.html")


def complaintfunction(request):
    return render(request, "complaint.html")


def login(request):
    return render(request, "login.html")


def voting(request):
    return render(request, "voting.html")


def checkaminlogin(request):
    aminuname = request.POST["uname"]
    aminpwd = request.POST["pwd"]
    flag = signup.objects.filter(Q(username=aminuname) & Q(password=aminpwd))
    if flag:
        return render(request, "index.html")
    else:
        return render(request, "loginfail.html")


def createuser(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        password = request.POST['password']
        email = request.POST['email']
        s = signup(username=uid, password=password, email=email)
        signup.save(s)
        msg = 'Registration is Succesful'
        return render(request, 'login.html', {'msg': msg})


def singup(request):
    return render(request, 'signup.html')



def createregister(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        adhar_number = request.POST.get('adhar_number')
        # qualification = request.POST.get('qualification')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        # gender = request.POST.get('gender')
        address = request.POST.get('address')

        new_registration = createregister(
            fullname=full_name,
            adharnumber=adhar_number,
            # educationalqualificatiom=qualification,
            phonenumber=phone_number,
            # gender=gender,
            birthdate=birth_date,
            address=address
        )
        # Save the new registration to the database
        new_registration.save()

        return redirect('success_page')

    return render(request, 'voterregistration.html')


