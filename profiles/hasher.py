from __future__ import absolute_import
from django.test.utils import override_settings
from django.conf import settings
from allauth.utils import get_user_model
from allauth.account.models import EmailAddress
from django.urls import reverse


@override_settings(
    ACCOUNT_DEFAULT_HTTP_PROTOCOL='https',
    ACCOUNT_EMAIL_VERIFICATION=settings.EmailVerificationMethod.MANDATORY,
    ACCOUNT_AUTHENTICATION_METHOD=settings.AuthenticationMethod.USERNAME,
    ACCOUNT_SIGNUP_FORM_CLASS=None,
    ACCOUNT_EMAIL_SUBJECT_PREFIX=None,
    LOGIN_REDIRECT_URL='/account/profile/',
    ACCOUNT_ADAPTER='allauth.account.adapter.DefaultAccountAdapter',
    ACCOUNT_USERNAME_REQUIRED=True)

@override_settings(
    ACCOUNT_AUTHENTICATION_METHOD=settings.AuthenticationMethod
        .USERNAME_EMAIL)
def test_username_containing_at(self):
    user = get_user_model().objects.create(username='@santana.allen')
    user.set_password('woot')
    user.save()
    EmailAddress.objects.create(user=user,
                                email='santana.allen@gmail.com',
                                primary=True,
                                verified=True)
    resp = self.client.post(reverse('account_login'),
                            {'login': '@santana.allen@gmail.com',
                             'password': 'woot'})
    self.assertRedirects(resp,
                         'http://testserver'+settings.LOGIN_REDIRECT_URL,
                         fetch_redirect_response=False)
