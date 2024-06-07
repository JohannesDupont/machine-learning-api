FROM python:3.12-slim

WORKDIR /app

COPY mlops_problem/app.py app/

COPY mlops_problem/docker/requirements.txt . 

RUN apt-get update && apt-get install -y nano

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "app/app.py"]


