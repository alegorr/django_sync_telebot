#!/bin/bash
sudo docker build -t service1 . && docker run -p 8000:8000 --env-file=.env -it service1
# docker ps # show runned images
# sudo docker exec -it service1 sh # start shell inside the container
