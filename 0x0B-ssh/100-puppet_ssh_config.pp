# Client configuration file with Puppet
# Puppet to make changes in or config file

file { '/etc/ssh/ssh_config';
	ensure => present,   

content =>"

	#SSH client config
	Host* 
	IdentityFile ~/.ssh/school
	PasswordAuthentication no 
",
}
