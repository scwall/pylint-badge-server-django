# def main_page(request):
#     return render(request, template_name='index.html')
#
#
# @csrf_exempt
# def reports(request):
#     if request.method == 'POST':
#         travis_job_id = request.POST['travis_job_id']
#         pylint_report = request.FILES['pylint-report'].read().decode('utf-8')
#         pylint_token = jwt.decode(request.POST['pylint_badge_token'], SECRET_KEY, algorithms=['HS256'])
#         pylint_badge = get_rating_and_colour(pylint_report)
#
#         return HttpResponse('Ok', status=200)
#
#     return HttpResponse('bad request', status=400)
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect(reverse('engine:bottle_engine_admin'))
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})
#
# @login_required
# def user(request,username):
#     return HttpResponse("hello" + username )
import os

import jwt

from pylint_badge_server.settings import SECRET_KEY
from users.models import Repository

open('pylint.json')
token = jwt.encode({
    'user_id': 1,
    'repository_id': 1}, SECRET_KEY, algorithm='HS256').decode('utf-8')
# jwt.decode(
#     'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJyZXBvc2l0b3J5X2lkIjoyfQ.d5SFSvOldbaSjw30KdCI3tzM8LiXMhWSurjoJBglwKg',
#     SECRET_KEY, algorithms=['HS256'])
# test = Repository.objects.get(id=2)
# print(test.badge.name)
from pylint.models import Repository, Reports