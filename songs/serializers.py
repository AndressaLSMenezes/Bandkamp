from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
        read_only_fields = ["album_id"]
        extra_kwargs = {
            "id": {"read_only": True},
            "title": {"required": True},
            "duration": {"required": True},
            "album_id": {"required": True, "read_only": True},
        }
        depth = 1

