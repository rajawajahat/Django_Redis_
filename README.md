# django_redis_docker
This is the repository containing APP which is built using Django, Redis and containerized via Docker.

## Steps to setup on your machine:
- First install docker and docker-compose on your machine.
- Then run the <b>docker-compose build</b> command to create container(s) and install the prerequisites.
- Then run the <b>docker-compose up</b> command to start the project.

## Endpoints:
There are two endpoints which you can hit.
- Health check endpoint http://0.0.0.0:8000/metar/ping
- Get weather info endpoint http://0.0.0.0:8000/metar/info?scode=AABP
