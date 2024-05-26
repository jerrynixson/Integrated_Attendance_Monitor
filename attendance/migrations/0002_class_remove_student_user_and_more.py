# Generated by Django 5.0.6 on 2024-05-21 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='status',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='attendance.class'),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
