from typing import Optional

from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.StringRelatedField(many=True, read_only=True)

    def create(self, validated_data: dict) -> Optional[Movie]:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Optional[Movie]:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)

        instance.save()

        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=63)
    last_name = serializers.CharField(max_length=63)

    def create(self, validated_data: dict) -> Optional[Actor]:
        return Actor.objects.create(**validated_data)

    def update(self, instance: Actor, validated_data: dict) -> Optional[Actor]:
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name", instance.last_name
        )

        instance.save()

        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63)

    def create(self, validated_data: dict) -> Optional[Genre]:
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data: dict) -> Optional[Genre]:
        instance.name = validated_data.get("name", instance.name)

        instance.save()

        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=63)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data: dict) -> Optional[CinemaHall]:
        return CinemaHall.objects.create(**validated_data)

    def update(
            self,
            instance: CinemaHall,
            validated_data: dict
    ) -> Optional[CinemaHall]:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )

        instance.save()

        return instance
