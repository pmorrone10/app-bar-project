FROM python:3.9

#WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG es_ES.UTF-8
ENV LC_ALL es_ES.UTF-8
ENV LC_CTYPE es_ES.UTF-8
ENV LANGUAGE es_ES:es


COPY /app /app
COPY main.py .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]