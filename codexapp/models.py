from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    
    category_name = models.CharField(max_length=100, blank=False, null=False)
    
    def __unicode__(self):
        return self.category_name
    
class Information(models.Model):
    
    # caso nao queira usar o campo id padrao gerado pelo django
    #information_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    information = models.TextField(blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category)
    url = models.URLField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    

