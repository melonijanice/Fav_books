from login.models import User
from django.db import models


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) == "":
            errors["title"] = "Title is required"
        if len(postData['description']) < 5:
            errors["description"] = "Description should be atleast 5 characters"
        return errors

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uploaded_by=models.ForeignKey(User,related_name="uploaded_books",on_delete=models.CASCADE)
    add_to_fav_by=models.ManyToManyField(User,related_name="fav_books")
    objects=BookManager()
