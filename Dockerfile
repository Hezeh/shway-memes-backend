# Pull base image 
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /data
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh /code/entrypoint.sh

# Copy project
COPY . /code/

# run entrypoint.sh
ENTRYPOINT [ "/code/entrypoint.sh" ]
