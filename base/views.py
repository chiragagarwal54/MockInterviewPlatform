from django.shortcuts import render
from base.models import Company, MockSet, Question

def home(request):

    context = {}

    companies = Company.objects.all()
    context['company']=companies

    return render(request, 'home.html', context)

def companypage(request, companyid):

    context = {}

    mockset = MockSet.objects.filter(company_id=companyid)
    context['mockset']=mockset

    return render(request, 'companypage.html', context)

# Create your views here.
