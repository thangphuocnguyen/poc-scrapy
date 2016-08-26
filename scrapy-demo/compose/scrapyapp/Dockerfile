# #############################################
# This is dockerfile for local development
# #############################################

FROM python:3.5

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y git-core ssh vim

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/requirements.txt

WORKDIR /app
