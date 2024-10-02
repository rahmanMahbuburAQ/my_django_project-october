from rest_framework import serializers
from .models import Instructor, Course, Student, Enrollment, Transaction, Review
from django.contrib.auth.models import User

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Specify the fields you want to expose in the API

# Serializer for the Instructor model
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'bio', 'email', 'profile_image']

# Serializer for the Course model
class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)  # Nested Instructor data in Course

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'duration', 'level', 'language', 'instructor']

# Serializer for the Student model
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data in Student

    class Meta:
        model = Student
        fields = ['id', 'user', 'username', 'email']

# Serializer for the Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # Nested Student data in Enrollment
    course = CourseSerializer(read_only=True)  # Nested Course data in Enrollment

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'date_enrolled', 'completed']

# Serializer for the Transaction model
class TransactionSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # Nested Student data in Transaction
    course = CourseSerializer(read_only=True)  # Nested Course data in Transaction

    class Meta:
        model = Transaction
        fields = ['id', 'student', 'course', 'transaction_date', 'amount_paid']

# Serializer for the Review model
class ReviewSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # Nested Student data in Review
    course = CourseSerializer(read_only=True)  # Nested Course data in Review

    class Meta:
        model = Review
        fields = ['id', 'course', 'student', 'rating', 'comment', 'date_added']
