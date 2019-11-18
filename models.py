from django.db import models
from django.urls import reverse
# create models here

class Person(models.Model):
    '''Encapsulate concept of a person...'''
    name = models.TextField(blank=False)

    def __str__(self):
        '''return string representation of this person'''
        return self.name

class Quote(models.Model):
    '''Encapsulate idea of a quote'''

    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete="CASCADE")
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this obj'''
        return '"%s" - %s' % (self.text, self.person.name)
    def get_absolute_url(self):
        '''Return URL to display quote object'''
        return reverse("quote", kwargs={"pk": self.pk})
        

class Image(models.Model):
    '''represent an image...associated with a person.'''

    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete="CASCADE")

    def __str__(self):
        '''return string repre of this image'''
        return self.image_url
    
    
