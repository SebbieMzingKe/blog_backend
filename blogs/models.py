from pickle import TRUE

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

"""
from blogs.models import Blog
>>> new_blog1 = Blog(
... title = "ReactJS for lovers",
... content = "This is a video fo reactJS lovers")
class Post:
    id int
    title str(50)
    content text
    created date time
"""

User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default = "")
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")

    # string representationn of our blogs
    def __str__(self) -> str:
        return self.title
    
