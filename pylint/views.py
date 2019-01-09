from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):

    return render(request,template_name='index.html')

def report(request):
    if request.method == 'POST':
        travis_job_id = request.POST['travis_job_id']
        pylint_report = request.FILES
        pylint_badge_token = request.POST['pylint_badge_token']
    return HttpResponse('bad request', status=400)
