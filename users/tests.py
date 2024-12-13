
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
                        reverse('users:register'),
                         data = {
                             "username": "jaxxon",
                             "first_name": "Jakhon",
                             "last_name":"Xudoyberdiyev",
                             "email":"xudoyberdiyev33@gmail.com",
                             "password":"somepassword",
                         })

        user = User.objects.get(username="jaxxon")

        self.assertEqual(user.first_name, "Jakhon")
        self.assertEqual(user.last_name, "Xudoyberdiyev")
        self.assertEqual(user.email, "xudoyberdiyev33@gmail.com")
        self.assertTrue(user.check_password("somepassword")),

    def test_user_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data = {
                "first_name":'Jakhon',
                "last_name":"Xudoyberdiyev",
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertEquals(response.context['form'].errors['username'], ['This field is required.'])
        self.assertEquals(response.context['form'].errors['password'], ['This field is required.'])

    def test_invalid_email(self):
        response = self.client.post(
            reverse('users:register'),
            data = {
                "first_name":'Jakhon',
                "last_name":"Xudoyberdiyev",
                "email":"xudoyberdiyev",
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertEquals(response.context['form'].errors['email'], ['Enter a valid email address.'])


    def test