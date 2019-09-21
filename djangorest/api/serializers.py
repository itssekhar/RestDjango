from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """ Serialzers to map the model instance into the Json format.
    """

    class Meta:
        """ Meta class to map the serializer's fields with the model fields.
        """
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    
