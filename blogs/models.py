from django.db import models

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

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default = "")
    created = models.DateTimeField(auto_now_add=True)

    # string representationn of our blogs
    def __str__(self) -> str:
        return self.title
    
