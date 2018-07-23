from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model): #상속
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()#게시글
    created_data = models.DateTimeField(default=timezone.now)#timezone.now :지금시간
    published_data=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title