FROM python:3

WORKDIR /

COPY /src /src
COPY main.py /

RUN pip install -r /src/requirements.txt

RUN apt-get update
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

CMD python3 /main.py