from rest_framework import serializers

from music.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    # artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Artist
        # fields = ('id', 'name')
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        # fields = ('id', 'artist', 'title')
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = ('id', 'album', 'last_updated')
        fields = '__all__'
