from django.db import models
from datetime import date

class Show_manager(models.Manager):
    def basic_validator(self, postData):
        today = date.today()
        errors = {}
        if len(postData['title_input']) < 2:
            errors['title_input'] = 'Show title should be at least 2 characters'
        if len(postData['network_input']) < 3:
            errors['network_input'] = 'Network should be at least 3 characters long'
        if len(postData['desc_input'])>1 and len(postData['desc_input'])<10:
            errors['desc_input'] = 'Description must be at least 10 characters if it is not blank'
        if str(today) <= postData['release_date_input']:
            errors['release_date_input'] = 'Release date must be in the past'
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Show_manager()

