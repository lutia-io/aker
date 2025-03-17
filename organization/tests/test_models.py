from django.test import TestCase
from user.models import User
from organization.models import Organization


class OrganizationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.organization = Organization.objects.create(
            name="Test Organization", slug="test-organization", user=self.user
        )

    def test_organization_str(self):
        self.assertEqual(str(self.organization), "Test Organization")

    def test_organization_creation(self):
        self.assertEqual(self.organization.name, "Test Organization")
        self.assertEqual(self.organization.slug, "test-organization")
        self.assertEqual(self.organization.user, self.user)
