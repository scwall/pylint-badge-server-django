import jwt
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pylint_badge_server.settings import SECRET_KEY
from pylint.pylint_badge import get_rating_and_colour
import json

# Create your views here.
def main_page(request):

    return render(request,template_name='index.html')
@csrf_exempt
def reports(request):
    if request.method == 'POST':
        travis_job_id = request.POST['travis_job_id']
        pylint_report = request.FILES['pylint-report'].read().decode('utf-8')
        pylint_token = jwt.decode(request.POST['pylint_badge_token'], SECRET_KEY, algorithms=['HS256'])
        pylint_badge = get_rating_and_colour(pylint_report)

        return HttpResponse('Ok', status=200)

    return HttpResponse('bad request', status=400)
