from django.db import models

# Create your models here.
class Media(models.Model):
    name: models.CharField(max_length=120)
    dosage: models.CharField(max_length=20)
    taken: models.BooleanField(default=False)

    def _str_(self):
        return self.name
