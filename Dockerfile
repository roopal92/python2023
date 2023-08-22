FROM python:latest
RUN apt-get update && apt-get install -y --no-install-recommends\
    curl \
    unzip \
    wget \
    bash
WORKDIR /app
COPY . /app
COPY run.sh /app
RUN chmod +x run.sh
ENTRYPOINT [ "/bin/bash", "./run.sh" ]
