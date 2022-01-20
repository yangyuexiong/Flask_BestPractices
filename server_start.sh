#!/bin/bash

cd /srv/Flask_BestPractices

Flask_BestPractices_UUID=`docker ps | grep Flask_BestPractices | awk '{print $1}'`;

if [ $Flask_BestPractices_UUID ]; then
  docker stop $Flask_BestPractices_UUID;
  echo "stop success";
fi

echo y | docker system prune
docker build -t 'Flask_BestPractices' .
echo "build success"
docker run -d --network host --name Flask_BestPractices Flask_BestPractices
# docker run -d -p 5000:5000 --name Flask_BestPractices Flask_BestPractices
echo "run success"