from django.db import models


class Fail(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    year = models.PositiveSmallIntegerField()
    body = models.CharField(max_length=255)
    favorite_teacher = models.CharField(max_length=64)
    approved = models.NullBooleanField(default=None)

    class Meta:
        ordering = ['-date_created']

    def __unicode__(self):
        return self.body

