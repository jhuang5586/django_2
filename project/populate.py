import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

#FAKE POP SCRIPT
from app.models import User
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for person in range(N):

        user_name=fakegen.name().split()
        fake_first_name=user_name[0]
        fake_last_name=user_name[1]
        fake_email=fakegen.email()

        user=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
