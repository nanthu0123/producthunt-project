from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    title=models.TextField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField('images/')
    icon=models.ImageField('images/')
    votes_total=models.IntegerField(default=1)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')
