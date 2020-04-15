## Test Task
Python Developer Test Task

#### Implement URL Status Checker
* Clone this repository
```
git remote add origin git@github.com:nurbek-b/-----.git
```

* Activate virtual environment:
```
pip install pipenv
pipenv --python 3.7
pipenv shell
pipenv install
```

#### Database on db.sqlite

* Run command
```
python mamange.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
* Create some urls from admin page
* Run redis from on docker server
```
docker run -d -p 6379:6379 redis
```
* Run celery worker
```
celery -A url_status_checker worker -l info
```
* Run celery crontab
```
celery -A url_status_checker beat -l info

```