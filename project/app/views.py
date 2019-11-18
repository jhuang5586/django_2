from django.shortcuts import render
from app.models import User

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def users(request):
    user_list=User.objects.order_by('last_name')
    dict={'key':user_list}
    return render(request, 'app/users.html', context=dict)
