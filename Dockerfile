# base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
#RUN pip install pipenv && pipenv install --system
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Expose the port that Django will run on
EXPOSE 8081

# Run Django when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
