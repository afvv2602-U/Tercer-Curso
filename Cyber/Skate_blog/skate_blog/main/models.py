# main/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.urls import reverse

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.model(email=email, is_staff=True,
                          is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user
    

class CustomUserSB(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, unique=True, default=None)
    
    genero = models.CharField(max_length=10, choices=[(
        'm', 'Masculino'), ('f', 'Femenino'), ('o', 'Otro')], blank=True)
    
    
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    about_me = models.TextField(blank=True)
    accept_politics = models.BooleanField(default=False)
            
    direccion = models.CharField(max_length=100, blank=True)
    ciudad = models.CharField(max_length=50, blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    
    suscripcion = models.BooleanField(default=False)
    
    tarjeta_de_credito = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=20, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField(null=True,default=None)
    descripcion = models.CharField(max_length=250,null=True,default=None)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    suscripcion = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('ver_publicacion', args=[str(self.id)])
    
class Comentarios(models.Model):
    Publicacion = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto
    
