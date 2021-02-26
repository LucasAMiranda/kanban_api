from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'cards'
        fields = ('title', 'description', 'status')
