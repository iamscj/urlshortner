from django.db import models

# Create your models here.
#for creating server--> python manage.py runserver
#it's same as creating database named url having two columns 1st is link and and second is uuid
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid=models.CharField(max_length=10)
#after this part we use python manage.py makemigrations and python manage.py migrate command to migrate it to the database 

#now we are creating the superuser to manage the data base by using command python manage.py createsuperuser