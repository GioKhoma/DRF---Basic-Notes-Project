from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # amogiebs user fields modelebidan da danarchens gaushvebs
        exclude = ['user']
