from django.shortcuts import render

# Create your views here.

def all_interests(request):
    return render(request, 'interestpage/all_interests.html')


#kiv interest_home
def interest_home(request, interest_name):
    return render(request, 'interestpage/interest_home.html')

def index(request):
    return render(request,"interestpage/index.html")