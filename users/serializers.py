from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(
        source='group.name',
        read_only=True
    )
    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = Student
        fields = [
            'id', 'username', 'password', 'first_name',
            'last_name', 'email', 'middle_name', 'birth_date',
            'gender', 'phone', 'address', 'photo', 'student_id',
            'group', 'group_name', 'course', 'admission_year',
            'education_form', 'funding', 'status',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.set_password(password)
        student.save()
        return student

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance