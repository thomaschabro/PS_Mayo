from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'login'
    is_anonymous = False
    is_authenticated = True

    def __str__(self):
        return self.login


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks") # Quando um usuário for deletado, as tarefas associadas também serão deletadas

    def __str__(self):
        return self.title
