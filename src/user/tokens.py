from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

from src.api.serializers import ProfileSerializer


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()




def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': ProfileSerializer(user, context={'request': request}).data
    }