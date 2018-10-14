# _GoldenProfile_

## Using the Docker Container

To control the project on Docker-Containers follow this commands:

```shell
# Starting the containers
$ docker-compose up

# See the logs of the containers
$ docker-compose logs

# Stopping the containers
$ docker-compose stop
```

The first `docker-compose up` can take some while. There are some heavy dependencies which have to be downloaded.

After the containers are running you can find the ui under this URL: [http://localhost](http://localhost)


> If you changed something in the docker images you have to build the images again (`docker-compose build`). You don't have to rebuild if you only change the source code of the application itself - in this

## Run application local without Docker

1. Make sure you have python3 installed (`python3 --version`)
2. Move to the server directory
3. Pull all dependencies (`pip3 install -r requirements.txt`)
3. Run the server (`python3 run.py`)

> ⚠️ Attention ⚠️
>
> If there're are any missing packages, it's recommended to download them manually because some of the packages listed in the _requirements.txt_ are deprecated
