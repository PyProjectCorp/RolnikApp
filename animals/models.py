from django.db import models
from users.models import NormalUser

class Animals(models.Model):
    oznaczenie = models.CharField(max_length=100)
    TYP_CHOICES = (
    ('KROWA', 'Krowa'),
    ('SWINIA', 'Swinia'),
    ('KURA', 'Kura'),
    ('KACZKA', 'Kaczka'),
    ('GES', 'Ges'),
    ('INDYK', 'Indyk'),
    ('INNE', 'Inne'),
)
    typ = models.CharField(max_length=50,
                                      choices=TYP_CHOICES,
                                      default='KROWA')
    user = models.ForeignKey(NormalUser)
    old = models.IntegerField()
    weight = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.typ)