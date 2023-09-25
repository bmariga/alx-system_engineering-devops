# Set up my client config file
# using puppet to make changes to the default ssh config file

file { 'etc/ssh/ssh_config':
        ensure => present,

content => "

	#SSH client configuration
	#host *
	#IdentityFile ~/.ssh/school
	#PasswordAuthentication no
	",
}
