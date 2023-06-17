from django.db import models

# Create your models here.

class ToDoList(models.Model)  : 
	#each to do list will gonna have a name   
	name = models.CharField(max_length = 200)

	def __str__(self) : 
		return self.name

class Item (models.Model)  :
	#make conenctio n between both 
	todolist = models.ForeignKey(ToDoList ,on_delete=models.CASCADE)
	#each item will will have a text and  complete 
	text = models.CharField( max_length=300)
	done = models.BooleanField()
    
	def __str__(self) : 
		return self.text



