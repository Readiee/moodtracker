from django.contrib.auth.base_user import BaseUserManager
import secrets


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not login:
            raise ValueError('login должен быть указан')
        if not password:
            raise ValueError('password должен быть указан')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(login, password, **extra_fields)
