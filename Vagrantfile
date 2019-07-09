
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision :shell, :path => "bootstrap.sh"
  
  config.vm.synced_folder "vagrant/", "/home/vagrant", create: true

end
