
from django.contrib.auth import get_user
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

    def test_unique_username(self):

        user = User.objects.create(username="jaxxon", first_name="Jakhon", last_name="Xudoyberdiyev")
        user.set_password("qanaqadirpasswrod")
        user.save()

        response = self.client.post(
            reverse('users:register'),
            data = {
                "username": "jaxxon",
                "first_name": "Jakhon",
                "last_name":"Xudoyberdiyev",
                "email":"xudoyberdiyev33@gmail.com",
                "password":"somepassword",
            })

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertEquals(response.context['form'].errors['username'], ["A user with that username already exists."])


class LoginTestCase(TestCase):
    def setUp(self):
        db_user = User.objects.create(username="jaxxon", first_name="Jakhon")
        db_user.set_password("somepassword")
        db_user.save()

    def test_user_successful_login(self):
        self.client.post(
            reverse('users:login'),
            data = {
                "username": "jaxxon",
                "password": "somepassword",
            }
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_user_logout(self):
        self.client.login(username="jaxxon", password="somepassword")
        self.client.get(reverse('users:logout'))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_invalid_credentilas(self):
        self.client.post(
            reverse('users:login'),
            data = {
                "username": "wrong-username",
                "password": "somepassword",
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        db_user = User.objects.create(username="jakxon", first_name="Jakhon", last_name="Xudoyberdiyev", email="xudoyberdiyev33@gmail.com")
        db_user.set_password("somepassword")
        db_user.save()

        self.client.post(
            reverse('users:login'),
            data = {
                "username": "jakxon",
                "password": "wrong-password",
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('users:login') + "?next=/users/profile/")

    def test_profile_details(self):
        user = User.objects.create(
            username="jaxxon",
            first_name="Jakhon",
            last_name="Xudoyberdiyev",
            email="xudoyberdiyev33@gmail.com",
        )
        user.set_password("somepasword")
        user.save()

        self.client.login(username="jaxxon", password="somepasword")
        response = self.client.get(reverse('users:profile'))
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

