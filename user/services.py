from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    def _create_user(self, cpf,password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not cpf:
            raise ValueError(_('The given cpf must be set'))

        user = self.model(cpf=cpf, is_staff=is_staff, is_active=True , is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, cpf, email=None, password=None, **extra_fields):
        return self._create_user(cpf, email, password, False, False, **extra_fields)

    def create_superuser(self, cpf, password, **extra_fields):
        user=self._create_user(cpf, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user