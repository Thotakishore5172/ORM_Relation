from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    language=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email

class Author(models.Model):
    name=models.CharField(max_length=100,blank=False,unique=True)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,blank=False)

    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    
class Collection(models.Model):
    name=models.CharField(max_length=100,blank=False,unique=True)

    def __str__(self) -> str:
        return self.name
    
class Books(models.Model):
    collection=models.ManyToManyField(Collection)
    title=models.CharField(max_length=100,blank=False)

    def __str__(self) -> str:
        return self.title