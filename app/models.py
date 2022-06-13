from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class GeneralUser(AbstractUser):
	userchoices = (
        (1,'ADMIN'),
        (2,'USER'),
    )
	full_name = models.CharField(max_length=500,null=True,blank=True)
	phone = models.CharField(max_length=50,null=True,blank=True,unique=True)
	usertype = models.IntegerField(default=2,choices=userchoices)

class Category(models.Model):
	category_name = models.CharField(max_length=500)

	def __str__(self):
		return self.category_name

class Quiz(models.Model):
	question = models.CharField(max_length=500)
	option_1 = models.CharField(max_length=500)
	option_2 = models.CharField(max_length=500)
	option_3 = models.CharField(max_length=500)
	option_4 = models.CharField(max_length=500)
	currect_answer = models.CharField(max_length=500)
	category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True,related_name="category")


class Result(models.Model):
	user_id = models.ForeignKey('GeneralUser', on_delete=models.CASCADE, null=True, blank=True,related_name="category")
	category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True,related_name="category_result")
	score = models.IntegerField()
	correct = models.IntegerField()
	wrong = models.IntegerField()