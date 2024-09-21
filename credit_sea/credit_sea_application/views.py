from django.shortcuts import render, HttpResponse, redirect
from credit_sea_app.models import Applicant
# Create your views here.


def create_applicant(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
    else:
        full_name = request.POST['full_name']
        need = request.POST['need']
        loan_tenure = request.POST['loan_tenure']
        employmnt_status = request.POST['employment_status']
        reason_for_loan = request.POST['reason_for_loan']
        employment_address = request.POST['employment_address']

        applicant = Applicant.objects.create(full_name = full_name, need = need, 
                                 loan_tenure = loan_tenure, employment_status = employmnt_status,
                                 reason_for_loan = reason_for_loan,
                                 employment_address = employment_address)
        
        applicant.save()

        return redirect("/user_dashboard")


def read_applicant(request):
   applicant = Applicant.objects.all()

   context = {}
   context['data'] = applicant
   return render(request, 'user_dashboard.html', context)
    

def verifier(request):
    verify = Applicant.objects.all()

    context = {}
    context['data'] = verify
    return render(request, 'verifier.html', context)


def loan(request):
    loan = Applicant.objects.all()

    context = {}
    context['data'] = loan
    return render(request, 'user_dashboard_loan.html', context)