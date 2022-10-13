#!/bin/bash

echo "Configure deployment"
if [ -f "./config/Dockerfile" ]; then
  echo "-> Docker"
  mv service1/settings.py config/heroku_settings.py
  mv requirements.txt config/heroku_requirements.txt
  mv config/docker_settings.py service1/settings.py
  mv config/docker_requirements.txt requirements.txt
  mv Procfile config/
  mv runtime.txt config/
  mv config/Dockerfile .
else
  echo "-> Heroku"
  mv service1/settings.py config/docker_settings.py
  mv requirements.txt config/docker_requirements.txt
  mv config/heroku_settings.py service1/settings.py
  mv config/heroku_requirements.txt requirements.txt
  mv config/Procfile .
  mv config/runtime.txt .
  mv Dockerfile config/
fi
