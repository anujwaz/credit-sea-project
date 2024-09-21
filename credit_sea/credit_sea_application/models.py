from django.db import models
from datetime import datetime, timezone

# Create your models here.

class Applicant(models.Model):

    full_name = models.CharField(max_length=200)
    need = models.CharField(max_length=200)
    loan_tenure = models.CharField(max_length=200)
    employment_status = models.CharField(max_length=200)
    reason_for_loan = models.CharField(max_length=200)
    employment_address = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
