# Pull base image 
FROM python:3.8.0-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /usr/src/app

# Set the working directory to /data
WORKDIR /usr/src/app

# Copy the current directory contents into the container
ADD . /usr/src/app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
