FROM python:3.12-slim

WORKDIR /home/jovyan/work

ADD . .

RUN apt-get update && apt-get install -y gcc python3-dev

RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get remove --purge --auto-remove -y gcc libc6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
