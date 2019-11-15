from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Todo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.task.title
