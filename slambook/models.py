from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CharacterTemplate(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cq_template=models.CharField(max_length=32)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.pk, self.cq_template)
    
    
class CQuestion(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        cquestion=models.TextField()
        date_time=models.DateTimeField(auto_now_add=True, blank=True)
        
        def __str__(self):
            return self.cquestion
        
        
class RCTemplateCQuestions(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        ctemplate=models.ForeignKey(CharacterTemplate,on_delete=models.CASCADE)
        cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
        date_time=models.DateTimeField(auto_now_add=True, blank=True)
        
        def __str__(self):
            return self.cquestion
        

class Slams(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    slam_name=models.CharField(max_length=32)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.slam_name
    
class Slam(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    slam=models.ForeignKey(Slams,on_delete=models.CASCADE)
    typ=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.cquestion.cquestion

    
class SlamChart(models.Model):
    fr=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='fr')
    to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to')
    slam=models.ForeignKey(Slams,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    mess=models.TextField(blank=True)
    is_fr=models.BooleanField(default=True)
    is_to=models.BooleanField(default=True)
    response=models.BooleanField(default=False)
    isreadslam=models.BooleanField(default=False)
    rmess=models.TextField(blank=True)
    
    
class Answer(models.Model):
    slamchart=models.ForeignKey(SlamChart,on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    ans=models.BigIntegerField(blank=True)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)

    
    
    
