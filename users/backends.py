from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import User

class UserBackend(ModelBackend):
    
    def authenticate(self,username=None,password=None, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password,user.password):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            # User().set_password(password)
            pass
        
        def get_user(self, user_id):
            User = get_user_model()        
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return None



    
        # def authenticate(self,request,email=None,password=None):
        #     if email and password:
        #         try:
        #             user = User.objects.get(email=email)
        #             if user.check_password(password,user.password):
        #                 if user.is_active:
        #                     return user
        #         except User.DoesNotExist:
        #             return None
        #     return None

        # def get_user(self,user_id):
        #     try:
        #         return User.objects.get(pk=user_id)
        #     except User.DoesNotExist:
        #         return None

    