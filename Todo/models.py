from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(
        max_length = 100,
        default = "",
        blank = False,
        null= False,
        
    )

    created = models.DateTimeField(
        "作成日時",
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        "更新日時",
        auto_now = True,
    )
def __str__(self):
    return self.todo