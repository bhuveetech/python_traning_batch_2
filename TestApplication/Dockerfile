# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
COPY requirements.txt  /tmp/requirements.txt

ADD . /app

RUN ls -l
# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt

# Expose 5000 port
EXPOSE 5000

# execute the Flask app
CMD ["python", "app.py"]