from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # not storing the username as a string
    config = models.JSONField(null=True, blank=True) # did it as a json until we decide
    def __str__(self):
        return str(self.id)