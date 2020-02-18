# Pull base image 
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME /app
ENV PORT 8080

# Set the working directory to /data
WORKDIR $APP_HOME
COPY . ./

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /$APP_HOME/
RUN pipenv install --skip-lock --system --dev

COPY --from=gcr.io/berglas/berglas:latest /bin/berglas /bin/berglas

# Run the web service on container startup. 
# Use gunicorn webserver with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec /bin/berglas exec -- gunicorn --bind :$PORT --workers 1 --threads 8 core.wsgi:application

