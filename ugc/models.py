from django.db import models

class Words(models.Model):
    GENDERS = [
        ['der', 'Der'],
        ['das', 'Das'],
        ['die', 'Die'],
    ]

    word = models.CharField(verbose_name='Word', max_length=100)
    gender = models.CharField(verbose_name='Gender', max_length=3, choices=GENDERS)

    def __str__(self):
        return self.gender + ' ' + self.word