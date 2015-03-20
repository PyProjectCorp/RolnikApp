from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Homepage(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    stopka = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.title)