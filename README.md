# wb95DjangoApp - Full stack Django website.
Simple Django site that was used as a portfolio website as well as blog for related topics.

## Technologies
* python3
* django
* sqlite3

## Getting Started
### Prerequisites
Requires python3

### Installing
Create a virtualenv (Optional).
```
> python -m venv VENVNAME
```

Activate the venv, depending on you terminal/command prompt/shell this will be different.
(For Powershell make sure you have script execution permisions.)
```
> \venv\Scripts\Activate.ps1
```

Install the dependancies.
```
> pip install -r requirements.txt
```

Migrate the database.
```
> python manage.py makemigrations
```

Perform the migration.
```
> python manage.py migrate
```

Create super user to add things to database (Optional).
```
> python manage.py createsuperuser
```

##Run the app
```
> python manage.py runserver
```

Access the admin backend by appending "/admin" to localhost.
