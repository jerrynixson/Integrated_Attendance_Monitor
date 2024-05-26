from django.shortcuts import render
from .models import Class, AttendanceRecord
from django.http import JsonResponse

def dashboard(request):
    return render(request, 'attendance/dashboard.html')

def mark_attendance(request):
    classes = Class.objects.all()
    return render(request, 'attendance/mark_attendance.html', {'classes': classes})

def view_attendance(request):
    classes = Class.objects.all()
    return render(request, 'attendance/view_attendance.html', {'classes': classes})

def get_class_records(request, class_id):
    records = AttendanceRecord.objects.filter(student__class_id=class_id).select_related('student')
    data = [
        {
            'student_name': record.student.name,
            'date': record.date.strftime('%Y-%m-%d'),
            'status': record.status
        }
        for record in records
    ]
    return JsonResponse(data, safe=False)
