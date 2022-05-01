# Django Start

```shell
pip3 install django
```

## New PROJECT + APP

```shell
django-admin startproject <PROJECT_NAME>
django-admin startapp <APP_NAME>
```

### add new APP to INSTALLED_APPS

edit settings.py add <APP_NAME> to INSTALLED_APPS = []

### Include URLS from APP

create urls.py inside APP folder

add

```python
urlpatterns = [
    path("", views.index, name="index"),
    ]
```

update urls.py inside PROJECT folder

add 

```python
path('', include("<APP_NAME>.urls"))
```

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls"))
]
```

## Migrations

edit models.py

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```