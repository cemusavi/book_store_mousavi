from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import models as auth_models

<<<<<<< HEAD
from lib import rename_files
from accounts.utils import validators
from lib.shared_models import BaseModel
=======
from utils import rename_files
from utils import validators
from utils.shared_models import BaseModel
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin, BaseModel):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_('username'),
                                max_length=150,
                                unique=True,
                                help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                validators=[username_validator],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                },
                                )

    first_name = models.CharField(_('first name'),
                                  max_length=150,
                                  blank=True,
                                  null=True,
                                  default=_('unknown'))

    last_name = models.CharField(_('last name'),
                                 max_length=150,
                                 blank=True,
                                 null=True,
                                 default=_('unknown'))

    email = models.EmailField(_('email address'),
                              unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              },
                              )

    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'),
                                   )

    is_active = models.BooleanField(_('active'),
                                    default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ),
                                    )

    phone_number = models.CharField(_('Phone number'),
                                    max_length=11,
                                    blank=True,
                                    null=True,
                                    validators=[validators.phone_number_validator])

    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(_('Avatar'),
                               upload_to=rename_files.rename_profile,
                               blank=True,
<<<<<<< HEAD
                               null=True,
                               default='one.jpg'
                               )
=======
                               null=True)
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

    objects = auth_models.UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return f'{self.first_name + " " + self.last_name}'

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username
