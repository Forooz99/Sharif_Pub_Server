# base image
FROM python:3.10

# Set environment variables
# Python output is sent straight to the terminal without being buffered,
# allowing for real-time visibility of the application's output and logs
# prevents python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevents python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY Pipfile Pipfile.lock /serverCode/
RUN pip install --upgrade pip
# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /serverCode

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ./sourceCode/entrypoint.sh
RUN chmod +x ./sourceCode/entrypoint.sh

# copy whole project to your docker home directory
COPY . serverCode

# Expose the port that Django will run on
EXPOSE 8000

# Run Django when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Run these commands:
# docker build -t Sharif_Pub_Server .
# docker run -it -p 8000:8000 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=123 -e DJANGO_SUPERUSER_EMAIL=admin@example.com Sharif_Pub_Server