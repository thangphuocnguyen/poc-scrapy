#!/bin/bash

service tor start
service privoxy start

if [ $1 ] && [ $1 == 'crawl' ]; then
    scrapy crawl $2
elif [ $1 ] && [ $1 == 'shell' ]; then
    scrapy shell $2
else
    /bin/bash
fi

bash -c "ls -la && python3 -m http.server 8000"
