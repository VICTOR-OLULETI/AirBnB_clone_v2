# update package repository
exec {'update':
  provider => 'shell',
  command  => 'apt-get -y update',
}
