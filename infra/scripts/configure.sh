#!/bin/bash
cd /home/ubuntu/aws-test/infra/configs
sudo cp nginx/nginx.conf /etc/nginx
sudo cp -r nginx/conf.d /etc/nginx
sudo cp systemd/gunicorn.socket /etc/systemd/system
sudo cp systemd/gunicorn.service /etc/systemd/system