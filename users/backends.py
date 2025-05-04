from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(phone_number=username)
            except UserModel.DoesNotExist:
                user = UserModel.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        return None