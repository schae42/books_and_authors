from django.db import models

# Create your models here.
class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Author object: {self.first_name} ({self.last_name})>"

class Books(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.CharField(max_length=255)
    authors = models.ManyToManyField(Authors, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Book object: {self.title} ({self.desc})>"