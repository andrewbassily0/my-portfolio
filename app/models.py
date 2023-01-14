from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField 

class Posts(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    description = RichTextField(blank=True , null=True)
    #description = models.TextField(max_length=2000)
    new = models.BooleanField(default=True)
    slug = models.SlugField(blank=True , null=True)
    image= models.ImageField(upload_to='media/' , blank=True)
    category = models.ForeignKey('category', related_name='category' ,on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-created', ) 

    def get_absolute_url(self):
        return reverse('posts:detail' , args=[self.slug])

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = 'category'

    def get_absolute_url(self):
        return reverse('posts:detail' , args=[self.slug])

    def __str__(self):
        return self.name

class profile (models.Model):
    profile= RichTextField()

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

