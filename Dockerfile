# set base image (host OS)
FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ .
CMD [ "python3", "./manager.py" ]