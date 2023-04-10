# update package repository
exec {'update':
  provider => 'shell',
  command  => 'sudo apt-get -y update',
}

# upgrade your packages
exec {'upgrade':
  provider => 'shell',
  command  => 'sudo apt-get -y upgrade',
}

# install nginx
package { 'nginx':
  ensure => installed,
}

# ensure the index.nginx-debian.html contains hello world
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!\n',
}

# create symlink
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

# change ownership
file { '/data/':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# configure nginx
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

    error_page 404 /404.html;

    location /404 {
	root /var/www/html;
	internal;
    }
}
',
}

# Restart nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/sites-enabled/default'],
}

# restart nginx service
#exec { 'nginx service':
#  provider  => 'shell',
#  command   => 'sudo service nginx restart',
#}
