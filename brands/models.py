from django.db import models


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Brand(models.Model):
    name = NameField(max_length=200)

    def __str__(self):
        return self.name
