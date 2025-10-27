from rest_framework import serializers
from veiculo.models import Veiculo


class SerializadorVeiculo(serializers.ModelSerializer):
    veiculo_novo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Veiculo
        fields = ['id', 'marca', 'modelo', 'ano', 'cor', 'combustivel', 'foto', 'veiculo_novo']

    def get_veiculo_novo(self, obj):
        return obj.veiculo_novo