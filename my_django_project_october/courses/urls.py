from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    InstructorViewSet,
    StudentViewSet,
    EnrollmentViewSet,
    TransactionViewSet,
    ReviewViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'instructors', InstructorViewSet, basename='instructor')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'reviews', ReviewViewSet, basename='review')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
