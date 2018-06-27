from rest_framework import serializers
from . models import Combine

class CombineSerializer(serializers.ModelSerializer):

	class Meta:

		model=Combine
		fields='__all__'