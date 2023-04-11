# Employee Management System <img src="https://icon-icons.com/icons2/2107/PNG/32/file_type_django_icon_130645.png" alt="django-icon" width="30">

A simple Django application that allows you to manage employee data with a user-friendly interface.

<!-- Add table of contents -->
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<!-- Add features list -->
## Features
- <img src="https://img.icons8.com/metro/26/000000/user-male-circle.png"/>" alt="users-icon" width="30"> User-friendly interface for managing employee data.
- <img src="https://img.icons8.com/metro/26/000000/edit.png"/>" alt="edit-icon" width="30"> Add, edit, and delete employee information.
- <img src="https://img.icons8.com/metro/26/000000/edit.png"/>" alt="filter-icon" width="30"> Filter employee data by various attributes such as position.

<!-- Add installation instructions -->
## Installation

To get started with Employee Management System, you need to have Python and pip installed on your system. Then, follow these steps:

1. Clone this repository:
```python
git clone https://github.com/msdqhabib/Employee-Management-System-Django.git
```
2. Navigate to the project directory:
```python
cd Employee-Management-System-Django
```
3. Install the required packages:
```python
pip install -r requirements.txt
```
4. Download and Install the Postgres SQL database:
```python
# Download Postgres SQL installer
# Install Postgres SQL by following the installer instructions
```
5. Configure Postgres SQL in settings.py file:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'EmployeeDB', #Db name specified in pg admin tool
        'USER': 'postgres', #default user is postgres
        'PASSWORD': '2432', #the password you set during installation of Postgres SQL installer
        'HOST': 'localhost', #if we are using DB locally
    }
}
```
6. Apply the database migrations:
```python
python manage.py makemigrations
python manage.py migrate
```
7. To run App migrations:
```python
#To migrate app Tables
python manage.py makemigrations app_name
python manage.py sqlmigrate app_name 0001 #0001 is migration file name

#Migrate all changes to DB:
python manage.py migrate
```
8. Run the development server:
```python
python manage.py runserver
```


The application will now be available at `http://localhost:8000`.

## Usage
Some usage points for this System
1. Easily manage employee data with a user-friendly web interface
2. Add, edit, and delete employee information from a centralized location
3. Keep track of employee performance metrics, such as attendance and productivity

## Contributing

If you would like to contribute to the Employee Management System, you can follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and add tests if possible.
4. Submit a pull request.

## License

The Employee Management System is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
