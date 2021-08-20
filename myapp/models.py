from django.db import models
from django.utils import timezone
# Create your models here.


class DB_href(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class DB_notice(models.Model):
    ctime = models.DateTimeField('保存日期', default=timezone.now())
    content = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.content)
