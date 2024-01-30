# Setup New Ubuntu server with nginx
# and add a custom HTTP header

package { 'nginx':
	ensure  => 'installed',
	require => Exec['update_store']
}

exec { 'update_store':
        command => '/usr/bin/apt-get update',
}

file {'/var/www/html/index.html':
	content => 'Hello World!',
	require => Service['nginx']
}

exec {'redirect_me':
	command  => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
	require  => File['/var/www/html/index.html']
}

exec {'HTTP header':
	command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
	require  => Exec['redirect_me']
}

service {'nginx':
	ensure  => running,
	require => Package['nginx']
