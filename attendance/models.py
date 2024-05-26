from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students', default=1)

    def __str__(self):
        return self.name

class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10)  # e.g., "Present", "Absent"

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
