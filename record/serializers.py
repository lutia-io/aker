from rest_framework import serializers
from record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            "uuid",
            "data",
            "created_at",
            "updated_at",
        ]
