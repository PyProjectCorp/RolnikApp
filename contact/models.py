from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    
    # def __unicode__(self):
    #     return '{} {} {}'.format(self.email, self.name, self.message)
    
    def __str__(self):
        return "Message from {name}".format(name=self.email)