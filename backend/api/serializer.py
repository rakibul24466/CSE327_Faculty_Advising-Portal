from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    

class EmailSerializer(serializers.Serializer):
    mail = serializers.EmailField()
    created = serializers.DateTimeField()
    
