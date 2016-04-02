#
# DJANGO PYTHON DOCKERFILE
#
# The following runs a python Django application using Nginx, Gunicorn & Supervisord
#

FROM ubuntu:14.04

MAINTAINER @modernfidelity

# The following Github repos act as reference for running Django on Docker in AWS EB :
#  - https://github.com/AndrewSmiley/django-docker-eb
#  - https://github.com/glynjackson/django-docker-template


# Install Python Setuptools and some other tools for working with this container if attached to it

# RUN apt-get install -y tar git curl vim wget dialog net-tools build-essential python-distribute
# RUN apt-get install -y curl build-essential
RUN apt-get update &&  apt-get install -y nginx supervisor \
                        python python-dev python-pip python-virtualenv \
                        libmysqlclient-dev \
                        libjpeg8-dev


# Copy the contents of this directory over to the container at location /src
ADD . /src


# Setup Django install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src && pip install -r /src/requirements.txt


# Setup Nginx
RUN rm /etc/nginx/sites-enabled/default
COPY deployment/django.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/django.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf


# The port we are exposing needs to match the port we are binding NGINX too.
# Nginx then talks to Gunicorn which runs the django WSGI
EXPOSE  9000

# Set the working directorly
WORKDIR /src

# Start processes. (Command to execute when we run the contaner)
CMD supervisord -c /src/deployment/supervisord.conf

#CMD ["/usr/bin/supervisord"]
