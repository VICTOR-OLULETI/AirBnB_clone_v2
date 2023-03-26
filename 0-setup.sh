#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p '/data/'
sudo mkdir -p '/data/web_static/'
sudo mkdir -p '/data/web_static/releases/'
sudo mkdir -p '/data/web_static/shared/'
sudo mkdir -p '/data/web_static/releases/test/'
echo -e "<html>\n<head>\n<\head>\n<body>Holberton School</body></html>" > '/data/web_static/releases/test/index.html'
sudo rm -f /data/web_static/current
sudo ln -s '/data/web_static/releases/test' '/data/web_static/current'
sudo chown ubuntu:ubuntu /data/
sed -i 's|root /var/www/html;|root /var/www/html;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|' /etc/nginx/sites-enabled/default
sudo nginx -s restart

