# Attendance Management Portal
A web-based application designed to streamline and manage attendance for schools/ colleges efficiently. Built using Django, this portal supports **API-based interaction** for seamless integration and flexibility.

## Features
* Admin Dashboard: Manage users, classes, and attendance records.
* Teacher Functionality: Mark attendance, view class attendance reports.
* Secure Authentication: Access control for authorised users only.
* API Support: Fully functional APIs to view and update attendance data programmatically.






## API Reference

#### Retrieve Attendance

```bash
  GET /api/attendance/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `class_id`| `int`    | **Required**. Class id     |
| `date`    | `int`    | **Required**. Date         |

#### Update Attendance

```bash
  GET /api/attendance/mark/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `class_id`| `int`    | **Required**. Class id            |
| `student_id`| `int`    | **Required**. Student id     |
| `status`  | `string` | **Required**. Present/ Absent     |
| `date`    | `int`    | **Required**. Date                |


## Screenshots
![image](https://github.com/user-attachments/assets/03da9f0d-54b6-400c-bc43-9fb694e4b68c)
![image](https://github.com/user-attachments/assets/e6fddee5-b141-454a-9d20-ab91eeae8189)

## Installation

#### Prerequisites
* Python 3.8+
* pipenv or virtualenv (recommended for environment management)

#### Setup
1. Clone repo:
```bash
  git clone https://github.com/jerrynixson/Integrated_Attendance_Monitor.git
```
2. Activate virtual environment:
```bash
  python -m venv venv
  source venv/bin/activate # For Windows: venv\Scripts\activate
```
or
```bash
  pipenv shell
```
3. Install dependencies:
```bash
  pip install -r requirements.txt
```
4. Run database migrations:
```bash
  python manage.py migrate

```
5. Create a superuser (admin account):
```bash
  python manage.py createsuperuser
```
6. Start the development server:
```bash
  python manage.py runserver
```
## Usage

* Admin: Log in using the superuser account to configure classes, teachers, and students.
* Teachers: Log in to mark attendance and view class-specific records.

* API usage: Connect through built in API to automatically add 


