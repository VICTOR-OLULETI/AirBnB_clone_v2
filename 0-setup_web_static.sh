#!/usr/bin/env bash
# Install and configure nginx web server
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt install -y nginx
echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html
sudo mkdir -p '/data/web_static/shared/'
sudo mkdir -p '/data/web_static/releases/test/'
sudo touch '/data/web_static/releases/test/index.html'
echo -e "<h1>Hello MyWorld!<\h1>" > '/data/web_static/releases/test/index.html'
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}
	location /redirect_me {
		return 301 https://youtube.com;
	}
	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-enabled/default

service nginx restart
