# #############################################
# This is dockerfile for local development
# #############################################

FROM python:3.5

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y git-core ssh vim tor privoxy
ADD ./compose/scrapyapp/privoxy.conf /etc/privoxy/config

RUN apt-get install -y build-essential curl python-dev libffi-dev libssl-dev libxml2-dev libxslt-dev

ADD ./compose/scrapyapp/entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod 700 /usr/bin/entrypoint.sh

EXPOSE 6800 8118 9050

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT /usr/bin/entrypoint.sh
