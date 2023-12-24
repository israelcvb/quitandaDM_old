from rest_framework import serializers
from ensaios.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'nome', 'feito', 'criado_em']