docker build -t jupyter-lab data_science_problem/docker/
docker run -d --rm -p 10000:8888 --env-file .env -v model_storage:/home/jovyan/work/models -v $(pwd)/data_science_problem:/home/jovyan/work --name jupyter-lab jupyter-lab

VOLUME_NAME="model_storage"

VOLUME_EXISTS=$(docker volume ls --format "{{.Name}}" | grep -w $VOLUME_NAME)

if [ -z "$VOLUME_EXISTS" ]; then
    echo "Creating Docker volume: $VOLUME_NAME"
    docker volume create $VOLUME_NAME
else
    echo "Docker volume $VOLUME_NAME already exists"
fi

