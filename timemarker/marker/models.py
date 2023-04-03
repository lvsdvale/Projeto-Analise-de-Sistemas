from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CompanyModel(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome', unique=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em ')

class TaskModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome')
    description = models.TextField(null=False, blank=False, verbose_name='Descrição')
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em ')

class SubTaskModel(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome')
    description = models.TextField(null=False, blank=False, verbose_name='Descrição')
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em ')

class TimerModel(models.Model):
    subtask = models.ForeignKey(SubTaskModel, on_delete=models.CASCADE)
    total_time_spent = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateField(auto_now_add=True, verbose_name='Criado em ')


class TimerMarkModel(models.Model):
    timer = models.ForeignKey(TimerModel, on_delete=models.CASCADE)
    started_at = models.DateField(auto_now_add=True, verbose_name='Iniciado em ')
    finished_at = models.DateField(auto_now_add=True, verbose_name='Finalizado em')
    time_spent = models.TimeField(auto_now=False, auto_now_add=False)



class UserManager(BaseUserManager):
    def Create_User(self, email, name, password=None):
        if not email:
            raise ValueError('Usuário deve ter um email')
        if not password:
            raise ValueError('Usuário deve ter uma Senha')
        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.name = name
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

class user(AbstractBaseUser):
    
    name = models.CharField(max_length=255, null=True, unique=True, help_text="Digite o seu nome COMPLETO", verbose_name="Nome")
    email = models.EmailField(max_length=255, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Cria em")
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_senha(self,senha):
        self.set_password(raw_password=senha)
        self.save()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']