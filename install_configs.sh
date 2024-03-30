#!/bin/bash
set -eo pipefail

cp configs/planets.socket /etc/systemd/system/planets.socket
cp configs/planets.service /etc/systemd/system/planets.service

cp configs/planets.nginx /etc/nginx/sites-available/planets
ln -s /etc/nginx/sites-available/planets /etc/nginx/sites-enabled/planets

systemctl enable planets.socket
systemctl enable planets.service
systemctl restart nginx
