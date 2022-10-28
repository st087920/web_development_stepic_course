from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')


class Question(models.Model):
  objects = QuestionManager()
  title = models.CharField()                                            
  text = models.CharField()
  added_at = models.TimeField()
  rating = models.IntegerField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, related_name='qstn_like_usr')
    

class Answer(models.Model):
  text = models.CharField()
  added_at = models.TimeField()
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
 
