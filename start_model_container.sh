docker build -f mlops_problem/docker/Dockerfile -t sensor-classifier .
docker run -d --env-file .env --name sensor-classifier -v model_storage:/app/models -p 8000:8000 sensor-classifier


