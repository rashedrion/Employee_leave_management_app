# Employee_leave_management_app
# Getting Started
You will need a few prerequisite to run the project locally


# git clone (https://github.com/rashedrion/Employee_leave_management_app.git)
create a virtual environment and activate it

1.pip install virtualenv  
# Now you have the virtualenv command (for all projects).

2.virtualenv env

Now you have a directory "env" in your project directory that will contain this project's virtualenv.

3.env\Scripts\activate

4.pip install django-heroku


5.pip install -r requirements.txt

6.python manage.py makemigrations

7.run migrations

8.python manage.py migrate

create a super user and put your password

9.python manage.py createsuperuser 

start the project

10.python manage.py runserver
