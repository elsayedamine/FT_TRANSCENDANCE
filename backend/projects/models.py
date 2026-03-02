# Create your models here.

import uuid
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    config = models.JSONField()  # scalable for synth patch config
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)