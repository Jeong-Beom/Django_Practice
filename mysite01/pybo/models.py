from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # 제목 최대글자수 제한
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # Add voter

    def __str__(self):
        return self.subject

class Answer(models.Model):
    ''' 
    CASCADE: Answer모델은 Question에 대한 답변에 해당하기에 Question모델을 속성으로 가져가야하며,
            질문이 삭제될 경우 답변도 삭제되어야하므로 Foreign Key를 사용해 해당 내용을 적용.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')