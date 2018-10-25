from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length=200) #짧은 문자열 정보를 저장(제목)
    text = models.TextField() #글자 수에 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title