# Employee_leave_management_app
# create virtual environment 
pip install virtualenv 

# Now you have the virtualenv command (for all projects).
virtualenv env

# Now you have a directory "env" in your project directory that will contain this project's virtualenv.

env\Scripts\activate

# Creates a requirements.txt that you can use to remember which packages need installing, and as input for

pip install -r requirements.txt
pip install django-heroku
# then need migration database 
python manage.py makemigrations
python manage.py migrate

# run the code.
python manage.py runserver
