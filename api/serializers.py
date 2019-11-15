from rest_framework import serializers
from app.models import Task, Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.CharField()

    class Meta:
        model = Todo
        fields = ['url', 'task', 'date', 'time', 'completed']

    def create(self, validated_data):
        task_name = validated_data.pop('task')
        task_instance, created = Task.objects.get_or_create(title=task_name)
        return Todo.objects.create(**validated_data, task=task_instance)
