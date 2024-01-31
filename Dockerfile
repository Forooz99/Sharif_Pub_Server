# base image
FROM python:3.10

# Set environment variables
# Python output is sent straight to the terminal without being buffered,
# allowing for real-time visibility of the application's output and logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /code
# copy whole project to your docker home directory
COPY . code

# Expose the port that Django will run on
EXPOSE 8000

# Run Django when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Run these commands:
# docker build -t Sharif_Pub_Server .
# docker run -it -p 8000:8000 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=123 -e DJANGO_SUPERUSER_EMAIL=admin@example.com Sharif_Pub_Server