<!-- Add header with project name and image -->
<h1 align="center">Employee Management System</h1>
<p align="center">
  <img src="https://placehold.it/400x200" alt="Project Image">
</p>

<!-- Add brief description of project -->
<p align="center">A simple Django application that allows you to manage employee data with a user-friendly interface.</p>

<!-- Add table of contents -->
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<!-- Add features list -->
## Features

- Add features according to this project

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

To use the Employee Management System, open your web browser and go to `http://localhost:8000`.

## Contributing

If you would like to contribute to the Employee Management System, you can follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Write your code and add tests if possible.
4. Submit a pull request.

## License

The Employee Management System is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
