
## Docker Hub commands
```
docker build -t $DOCKER_ACC/$DOCKER_REPO:version1.0 .
sudo docker push $DOCKER_ACC/$DOCKER_REPO:version1.0
docker login --username=yourhubusername --password=yourpassword

docker build -t testmailt46/simple-flask-api:version1.7 .
docker push testmailt46/simple-flask-api:version1.7
docker pull testmailt46/simple-flask-api:version1.0
```

## Docker Compose commands
```
docker-compose build
docker-compose up
docker-compose down
docker-compose up --force-recreate
docker-compose down --volumes
```

```
.\env\Scripts\activate
```

```
docker exec -it 05b3a3471f6f bash
root@05b3a3471f6f:/# psql -U postgres
postgres-# CREATE DATABASE mytest;
postgres-# \q
```


POSTGRES_USER=hello_flask
POSTGRES_PASSWORD=hello_flask
POSTGRES_DB=hello_flask_dev
DATABASE_URL=postgresql://hello_flask:password@localhost:5432/hello_flask_dev

DATABASE_URL=postgresql://unicorn_user:magical_password@localhost:5432/hello_flask_devrainbow_database



docker run --name some-postgres -e POSTGRES_PASSWORD=magical_password -d postgres


import psycopg2
conn = psycopg2.connect("dbname=test user=postgres")

import psycopg2
conn = psycopg2.connect("postgresql://unicorn_user:magical_password@localhost:5432/hello_flask_devrainbow_database")


# Spin up two container
```
docker-compose up -d --build
```

# Create table

```
docker-compose exec api python manage.py create_db
```

```
docker-compose down
```
