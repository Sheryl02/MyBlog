from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='uploads')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.RichTextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # category = models.CharField(max_length=100, default='Painting')
    category = models.ManyToManyField(Category, related_name='cats', default='Painting')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=str(self.id))

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length=100)
    your_comments = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.post.title
        return '%s - %s' % (self.post.title, self.name)
# Create your models here.
