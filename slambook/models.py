from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CharacterTemplate(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cq_template=models.CharField(max_length=32)
    
    def __str__(self):
        return '{} - {}'.format(self.pk, self.cq_template)
    
    
class CQuestion(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        cquestion=models.TextField()
        
        def __str__(self):
            return self.cquestion
        
        
class RCTemplateCQuestions(models.Model):
        user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
        ctemplate=models.ForeignKey(CharacterTemplate,on_delete=models.CASCADE)
        cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
        
        def __str__(self):
            return self.cquestion.cquestion
        

class Slams(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    slam_name=models.CharField(max_length=32)
    
    def __str__(self):
        return self.slam_name
    
class Slam(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cquestion=models.ForeignKey(CQuestion,on_delete=models.CASCADE)
    slam=models.ForeignKey(Slams,on_delete=models.CASCADE)
    typ=models.IntegerField()
    
    def __str__(self):
        return self.cquestion
    
    
class SlamChart(models.Model):
    fr=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='fr')
    to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to')
    slam=models.ForeignKey(Slams,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True, blank=True)
    mess=models.TextField(blank=True)
    is_fr=models.BooleanField(default=True)
    is_to=models.BooleanField(default=True)
    
    
