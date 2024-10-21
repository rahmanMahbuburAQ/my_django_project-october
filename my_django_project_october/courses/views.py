from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Instructor, Course, Student, Enrollment, Transaction, Review
from .serializers import InstructorSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer, TransactionSerializer, ReviewSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

# ViewSet for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet for Instructor
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# ViewSet for Course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    # Override retrieve method to return specific videos based on purchase status
    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()  # Get the requested course object
        user = request.user  # Get the currently logged-in user

        # Check if the user has purchased the course (in the Enrollment model)
        enrollment = Enrollment.objects.filter(student=user, course=course).first()

        if enrollment and enrollment.is_purchased:
            # If the course is purchased, return full access to paid videos
            course_data = {
                'id': course.id,
                'title': course.title,
                'description': course.description,
                'videos': course.paid_videos  # Return full paid videos
            }
        else:
            # If not purchased, return only access to free videos
            course_data = {
                'id': course.id,
                'title': course.title,
                'description': course.description,
                'videos': course.free_videos  # Return only free videos
            }

        return Response(course_data)

# ViewSet for Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ViewSet for Enrollment
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# ViewSet for Transaction
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# ViewSet for Review
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

