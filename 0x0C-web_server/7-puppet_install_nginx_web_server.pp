# Install Nginx package
package { 'nginx':
    ensure => installed,
}

# Start and enable Nginx service
service { 'nginx':
    ensure        => running,
        enable    => true,
          require => Package['nginx'],
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
    ensure         => file,
    content        => '
		server {
		             listen 80;
			server_name _;
			 location / {
			   return 301 http://$host/redirect_me;
				     }
			    location /redirect_me {
						           return 301 http://$host/;
								             }
							           }
	    ',
          require  => Package['nginx'],
            notify => Service['nginx'],
}

# Delete the default Nginx configuration symlink
file { '/etc/nginx/sites-enabled/default':
    ensure      => absent,
       require  => File['/etc/nginx/sites-available/default'],
         notify => Service['nginx'],
}
# Create the root content
file { '/var/www/html/index.html':
    ensure         => file,
        content    => 'Hello World!',
          require  => Package['nginx'],
            notify => Service['nginx'],
}

