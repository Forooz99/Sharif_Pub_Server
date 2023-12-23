# base image
FROM python:3.10

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt