from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, name, surname, badge, location, creationDate, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            name = name,
            surname = surname,
            fullName = name + ' ' + surname,
            badge = badge,
            location = location,
            creationDate = creationDate,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, surname, badge, location, creationDate, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name = name,
            surname = surname,
            fullName = name + ' ' + surname,
            badge = badge,
            location = location,
            creationDate = creationDate,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser):

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    full_name = models.CharField(max_length=51)
    badge = models.ImageField()
    location = models.CharField(max_length=25)
    creationDate = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
