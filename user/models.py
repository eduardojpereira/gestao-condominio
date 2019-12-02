from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .services import UserManager
import re



class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(_('CPF'), max_length=15, unique=True, help_text=_(
        'Requer. 14 characteres considerando as pontoaçoes. Exemplo xxx.xxx.xxx-xx'))
    first_name = models.CharField(_('nome'), max_length=30)
    last_name = models.CharField(_('sobrenome'), max_length=30)
    email = models.EmailField(_('email'), max_length=255, unique=True)
    apartamento = models.ForeignKey('apartamento.Apartamento', on_delete=models.CASCADE, null=True, blank=True)
    telephone = models.CharField(max_length=20)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designa se é um user leitor ou não.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designa si o user é ativo ou não, Deselecionar em vez de deletar as contas'))

    date_joined = models.DateTimeField(_('data inscrição'), default=timezone.now)
    date_inicio = models.DateField(_('data inicio moradia.'), null=True, blank=True)
    date_final = models.DateTimeField(_('data fim moradia.'), null=True, blank=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])