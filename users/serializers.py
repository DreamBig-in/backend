from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from allauth.account.utils import setup_user_email
from allauth.account.adapter import get_adapter
from users.models import User




class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True, write_only=True)
    google_id = serializers.CharField(required=True, write_only=True)


    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and User.objects.filter(email = email):
            raise serializers.ValidationError(
                _("A user is already registered with this email"))
        return email
  
    def custom_signup(self, request, user):
        pass
    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'password1': "randompassword",
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'google_id': self.validated_data.get('google_id', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.google_id = self.cleaned_data.get('google_id')
        user.save()
        return user