from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    content = models.CharField(max_length=255, unique=False)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tags")

    class Meta:
        ordering = ["done", "datetime"]

    def __str__(self):
        return self.content



