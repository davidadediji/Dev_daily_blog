from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length = 10000)

    def __str__(self):
        return self.title

if __name__ == "__main__":
    Post()