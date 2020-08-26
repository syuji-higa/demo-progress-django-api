from rest_framework import serializers
from machines.models import Machine

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('name', 'progress')
