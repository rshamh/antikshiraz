from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('کاربر باید شماره موبایل خود را وارد کند')

        user = self.model(
            username = username,
            
            # first_name = first_name,
            # last_name = last_name,
        )
        
        # user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            email = email,
            # first_name = first_name,
            # last_name = last_name,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^09?\d{9}$', message="Phone number must be entered in the format: '09*********'. Up to 11 digits allowed.")
    username = models.CharField(validators=[phone_regex], max_length=11, blank=False, unique=True, verbose_name='شماره تماس') # Validators should be a list
    

    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=50, unique=True, null=True, verbose_name='آدرس ایمیل')

    # required:
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # Special user
    special_user = models.DateTimeField(default=timezone.now, verbose_name='اشتراک ویزه تا')

    def is_special(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special.boolian = True
    is_special.short_description = 'کاربر ویژه'

    USERNAME_FIELD = 'username'

    # A list of the field names that will be prompted for when creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = ['email']  

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)




