from django.conf import settings
from django.db import models


class TTtest(models.Model):
    "Generated Model"
    ttest = models.BigIntegerField()
    tttt = models.BigIntegerField(
        null=True,
        blank=True,
    )
