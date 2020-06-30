from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Run(models.Model):
     distance = models.DecimalField(max_digits=6, decimal_places=2)
     start_Time = models.DateTimeField(auto_now=False, auto_now_add=False)
     end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

     def __str__(self):
          return f'''[{self.distance},{self.start_Time},{self.end_time},{self.user.username}]'''


class userFrends(models.Model):

     APPROVED = 'ap'
     PENDING = 'pn'
     DECLINE = 'dn'
     STATUS_CHOICES = [
          (APPROVED, 'approved'),
          (PENDING, 'pending'),
          (DECLINE, 'decline')
          ]
     status = models.CharField(
          max_length=2,
          choices=STATUS_CHOICES,
          default=PENDING,
     )
     user = models.ForeignKey(
          User, on_delete=models.CASCADE, related_name='following')
     frend = models.ForeignKey(
          User, on_delete=models.CASCADE, related_name='followed_by')


     def __str__(self):
          return f'''id : {self.id} - frendship between  {self.user} and  {self.frend} status {self.status}'''

class runLocations(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
     runID = models.ForeignKey(Run,on_delete=models.CASCADE, blank=True, null=True, related_name='runID')
     locations = models.TextField()

     def __str__(self):
          return f'''id :{self.id} - user :{self.user} - locations :{self.locations} runID : {self.runID.id}'''
