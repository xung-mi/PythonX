from rest_framework import serializers

class ReviewSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    review_text = serializers.CharField()
    rating = serializers.IntegerField(min_value=1, max_value=5) 