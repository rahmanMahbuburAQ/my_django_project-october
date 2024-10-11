from django.contrib import admin
from .models import Instructor, Course, Student, Enrollment, Transaction, Review

# Customizing the Instructor admin view
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Display fields in list view
    search_fields = ('name', 'email')  # Add a search box for name and email
    list_filter = ('email',)  # Add a filter by email

# Customizing the Course admin view
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'price', 'duration', 'level', 'instructor')  # Display key course info
    search_fields = ('title', 'instructor__name')  # Allow searching by title and instructor name
    list_filter = ('level', 'language')  # Filter by level and language

# Customizing the Student admin view
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user')  # Show user information
    search_fields = ('username', 'email')  # Search by username and email
    list_filter = ('user__email',)  # Filter by email

# Customizing the Enrollment admin view
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled', 'completed')  # Show enrollment details
    search_fields = ('student__username', 'course__title')  # Search by student and course title
    list_filter = ('completed', 'date_enrolled')  # Filter by completion status and enrollment date

# Customizing the Transaction admin view
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'transaction_date', 'amount_paid')  # Show transaction details
    search_fields = ('student__username', 'course__title')  # Search by student and course title
    list_filter = ('transaction_date',)  # Filter by transaction date

# Customizing the Review admin view
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating', 'date_added')  # Show review details
    search_fields = ('course__title', 'student__username')  # Search by course and student
    list_filter = ('rating', 'date_added')  # Filter by rating and date

# Register models to the admin interface
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Review, ReviewAdmin)

   

