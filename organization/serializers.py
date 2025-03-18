from rest_framework import serializers
from organization.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["uuid", "name", "slug", "created_at", "updated_at"]
