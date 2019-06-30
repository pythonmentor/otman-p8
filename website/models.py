from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

"""Authentification using the email instead of a username"""

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Product(models.Model):
    """ Product model """
    name = models.CharField(max_length=255, verbose_name="Nom du produit")
    category = models.TextField(verbose_name="Catégories")
    stores = models.CharField(max_length=200, null=True, verbose_name="Magasins")
    nutriscore = models.CharField(max_length=1, verbose_name="Score nutritionnel")
    url = models.URLField(verbose_name="URL du produit", unique=True)
    image_url = models.URLField(verbose_name="URL de l'image du produit", unique=True)
    image_small_url = models.URLField(verbose_name="URL de l'image du produit (Thumbnail)", unique=True)
    energy = models.FloatField(verbose_name="Valeur energétique")
    sugar = models.FloatField(verbose_name="Sucres pour 100g")
    salt = models.FloatField(verbose_name="Sels pour 100g")
    fat = models.FloatField(verbose_name="Gras pour 100g")
    saturated_fat = models.FloatField(verbose_name="Acides gras saturés pour 100g")
    sodium = models.FloatField(verbose_name="Sodium pour 100g")
    proteins = models.FloatField(verbose_name="Protéines pour 100g")
    carbohydrates = models.FloatField(verbose_name="Glucides pour 100g")
    saved = models.ManyToManyField(User,verbose_name="Utilisateurs ayant sauvegardés ce produit", default=1)

    class Meta:
        verbose_name = "produit"
        verbose_name_plural = "produits"
    
    def __str__(self):
        return self.name