# SwordsecBackendSolution
This is the solution repository for the Swordsec's interview question at https://github.com/Swordsec/challenge-questions/blob/master/backend/Kuyruklama.md

It has 4 Docker containers: flask, redis, redis worker, postgres

When flask server gets a `GET` request to `/add_user` endpoint, all of the users in the JSON files are getting written to postgres DB.


## Starting the Application


### Cloning the repo

```
git clone https://github.com/teooman/SwordsecBackendSolution.git
cd SwordSecBackendSolution
```

### Running the containers

```
docker compose build
docker compose up
```


The app should be running on `0.0.0.0:5000`

Go to http://0.0.0.0:5000/add_user to run the tasks

### Tests
The postgres container should create a postgres-data for the DB. The DB can also be checked with:

```
docker exec -it [container_id] sh
su - postgres
psql -U swordsecuser swordsec_test
```
