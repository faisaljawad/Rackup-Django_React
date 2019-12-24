from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def Create_User(self, email, username, password):
        user = self.model(username=username, email=email)
        user.set_password(password)
        return user

    def create_user(self, email, username, password):
        user = self.Create_User(email, username, password)
        user.save()

    def create_superuser(self, email, username, password):
        user = self.Create_User(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

    def create_staff_user(self, email, username, password):
        user = self.Create_User(email, username, password)
        user.is_staff = True
        user.is_superuser = False
        user.save()
