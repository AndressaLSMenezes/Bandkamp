from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
        # read_only_fields = ["user_id"]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True},
            "year": {"required": True},
            "user_id": {"required": True, "read_only": True},
        }
        depth = 1

