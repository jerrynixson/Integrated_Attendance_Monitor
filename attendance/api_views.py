from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Class, Student, AttendanceRecord
from .serializers import ClassSerializer, StudentSerializer, AttendanceRecordSerializer

@api_view(['GET'])
def list_students_by_class(request, class_id):
    student_class = get_object_or_404(Class, id=class_id)
    students = student_class.students.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_mark_attendance(request):
    data = request.data
    class_id = data.get('class_id')
    attendance_records = data.get('attendance_records')
    
    student_class = get_object_or_404(Class, id=class_id)
    for record in attendance_records:
        student = get_object_or_404(Student, id=record.get('student_id'), student_class=student_class)
        AttendanceRecord.objects.create(student=student, status=record.get('status'))
        
    return Response({'message': 'Attendance marked successfully'}, status=status.HTTP_201_CREATED)
