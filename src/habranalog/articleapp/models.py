from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=150)
    prememo=models.TextField(null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='articleapp/images',null=True,blank=True)
    data_published=models.DateField(auto_now_add=True)
    published=models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)+'__'+self.title
    
class ArticlesBlock(models.Model):
    title=models.CharField(max_length=150)
    prememo=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='articleapp/images',null=True,blank=True)
    data_published=models.DateField(auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)+'__'+self.title   
    
class Views(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    class Meta:
        unique_together=('user','article',)
    

    
