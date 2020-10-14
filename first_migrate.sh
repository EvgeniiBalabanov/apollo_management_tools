python manage.py makemigrations access_settings
python manage.py sqlmigrate access_settings 0001
python manage.py makemigrations test_application
python manage.py sqlmigrate test_application 0001
python manage.py makemigrations
python manage.py migrate