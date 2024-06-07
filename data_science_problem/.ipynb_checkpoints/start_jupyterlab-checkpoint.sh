docker build -t jupyter-lab docker/
docker run -d --rm -p 10000:8888 --env-file ../.env -v $(pwd):/home/jovyan/work --name jupyter-lab jupyter-lab
