DB_HOST=postgres_db

```bash
docker compose up -d
```

Migrations

After any changes in models create and apply migrations:

```bash
docker exec funnel  python manage.py makemigrations
docker exec funnel  python manage.py migrate

For filling data from CSV file:

```bash
docker exec funnel  python manage.py fill_data
```

For deleting all data from CSV file:

```bash
docker exec funnel  python manage.py delete_data
```

DB_HOST=localhost

```bash
docker compose -f inventory-compose.yml up -d
```

Sync migrations:

```bash
pipenv run python manage.py migrate
```

Create super user (Account with unlimited rights on admin panel):

```bash
pipenv run python manage.py  createsuperuser
```

Run app for development purposes:

```bash
pipenv run python manage.py runserver 8005
```


After any changes in models - migrations:

```bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```

For filling data from CSV file:

```bash
pipenv run python manage.py fill_data
```

For deleting all data from CSV file:

```bash
pipenv run python manage.py delete_data
```

## Additional commands

Delete all containers and flash all trash:

```bash
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker container prune -f
```

Delete all images:

```bash
docker image rm $(docker image ls -q) && docker image prune -af
```
