## Prerequisites:
+ [Docker](https://docs.docker.com/engine/installation/)
  > Docker is an open platform for developing, shipping, and running applications.

+ [Docker Machine](https://docs.docker.com/machine/install-machine/)

  > (For Mac/Windows)

  > Docker Machine is a tool that lets you install Docker Engine on virtual hosts, and manage the hosts with docker-machine commands.

+ [Docker Compose](https://docs.docker.com/compose/install/)

  > Compose is a tool for defining and running multi-container Docker applications.

*Notes: On case of using Mac/Windows, just only install [docker-toolbox](https://docs.docker.com/toolbox/overview/) to have all of three (Docker, Docker Compose, Docker Machine)*

## Getting up and run:

+ Clone the docker-django to your machine:

  ```
  $ git clone git@gitlab.asoft-python.com:g-thangnguyen/scrapy-training.git

  $ cd docker-django

  ```

+ Create the Machine (Optional)

  ```
  $ docker-machine create --driver virtualbox scrapydemo

  # Active machine
  $ eval $(docker-machine env scrapydemo)

  ```

+ Build/Boot the images

  ```
  $ docker-compose build

  $ docker-compose up

  ```

+ Directly remote and practice with scrapy

  ```
  # Get the container name

  $ docker-compose ps

  # Remote to container

  $ docker exec -it <container name> bash

  ```

## Scrapy commands:

  ```
  # Create scrapy project

  $ scrapy startproject <project name>


  # Access scrapy shell

  $ scrapy shell <url>

  ```

## Scrapy DEMO project:

  ```
  # Start GhostBlogSpider crawl project

  $ scrapy crawl ghost_blog_post


  # Export Item that crawled to JSON file

  $ scrapy crawl ghost_blog_post -o item-storage/ghost_blog_post.json


  # Export Related links that crawled from LxmlLinkExtractor to JSON file

  $ scrapy crawl ghost_spider -o item-storage/ghost_spider.json

  ```

## Notes:


