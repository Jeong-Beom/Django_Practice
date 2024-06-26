# load .bashrc
. ~/.bashrc

# activate virtual python environment
pyenv activate venv_mysite01

# add server execute file path
export DJANGO_SETTINGS_MODULE=config.settings.prod

# run serever
# python manage.py runserver 0:8000
