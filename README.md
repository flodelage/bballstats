# Bballstats
The purpose of this app is to allow non professional basketball teams to track its results and players stats like professional teams.

### Features
* Account management
* Capture players actions (convert in statistics) during a game
* Manage your teams
* Manage teams players
* See teams results and statistics (team stat and players stats)
* See teams average statistics for each season (team stat and players stats)

### Technologies
* Python / Django
* PostgreSQL
* Cloudinary

## Getting started
1. Clone the repository:
```
git clone https://github.com/flodelage/bballstats
```

2. Create virtual environnement:
```
pipenv install
```
3. Add python version in pipfile:
```
[requires]
python_version = "3.9"
```

4. Activate virtual environnement:
```
pipenv shell
```

5. Install requirements:
```
pipenv install -r requirements.txt
```

6. Create a .env file at the same level than manage.py, add and update following values variables (except DEBUG):
```
DEBUG=True

DJANGO_KEY=<your_django_key>

DB_NAME=<your_db_name>
DB_USER=<your_db_user_name>
DB_PASSWORD=<your_db_password>

CLOUD_NAME=<your_cloudinary_name>
CLOUD_KEY=<your_cloudinary_key>
CLOUD_SECRET=<your_cloudinary_secret>
```

7. populate the database:
```
python manage.py migrate
```
```
python manage.py populate_db
```

8. Run the project in local:
```
python manage.py runserver
```

9. Go to your browser in order to access the localhost at the URL (by default):
```
http://127.0.0.1:8000/
```

## Running tests
```
python manage.py test
```

