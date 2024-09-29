# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN apt-get install -y pulseaudio pulseaudio-utils
RUN pip install -v --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
