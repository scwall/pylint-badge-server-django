import jwt
from django.http import HttpResponse
from django.shortcuts import render
from pylint_badge_server.settings import SECRET_KEY
# Create your views here.
def main_page(request):

    return render(request,template_name='index.html')

def report(request):
    if request.method == 'POST':
        travis_job_id = request.POST['travis_job_id']
        pylint_report = request.FILES
        pylint_token = jwt.decode(request.POST['pylint_badge_token'], SECRET_KEY, algorithms=['HS256'])
        print(pylint_token)
    return HttpResponse('bad request', status=400)
