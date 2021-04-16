
## Docker Hub commands
```
docker build -t $DOCKER_ACC/$DOCKER_REPO:version1.0 .
sudo docker push $DOCKER_ACC/$DOCKER_REPO:version1.0
docker login --username=yourhubusername --password=yourpassword

docker build -t testmailt46/simple-flask-api:version1.0 .
docker push testmailt46/simple-flask-api:version1.0
docker pull testmailt46/simple-flask-api:version1.0
```

## Docker Compose commands
```
docker-compose build
docker-compose up
docker-compose down
```