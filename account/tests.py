from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AuthFlowTests(TestCase):
    def test_root_redirects_anonymous_user_to_registration(self):
        response = self.client.get(reverse('lawyer:home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account:register'))

    def test_admin_can_manage_lawyers(self):
        User = get_user_model()
        admin = User.objects.create_user(username='admin2', email='admin2@example.com', password='StrongPass123!')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()

        self.client.force_login(admin)
        response = self.client.get(reverse('lawyer:lawyer_list'))
        self.assertEqual(response.status_code, 200)
