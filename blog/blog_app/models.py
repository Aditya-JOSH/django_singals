from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.age}, {self.address}, {self.phone_number}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    views = models.IntegerField(default=0)
    news = models.BooleanField(default=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)