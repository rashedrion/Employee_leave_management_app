Getting Started
You will need a few prerequisite to run the project locally


git clone (https://github.com/rashedrion/Employee_leave_management_app.git)
create a virtual environment and activate it
pip install virtualenv  
Now you have the virtualenv command (for all projects).

virtualenv env
Now you have a directory "env" in your project directory that will contain this project's virtualenv.

env\Scripts\activate
pip install django-heroku


pip install -r requirements.txt
python manage.py makemigrations
run migrations

python manage.py migrate
create a super user and put your password

python manage.py createsuperuser --username=admin
start the project

python manage.py runserver
