Vagrant.configure(2) do |config|
  config.vm.define "web" do |web|
    web.vm.box = "centos"
web.vm.box_url = "C:/me/vagrant-centos-6.7.box"
web.vm.hostname = "centos"
    web.vm.network "private_network", ip: "192.168.56.10"
web.vm.provider "virtualbox" do |v|
  v.gui = false
  v.name = "centos"
  v.cpus = "1"
  v.memory = "2048"
end
  end
  
  config.vm.define "db" do |db|
    db.vm.box = "ubuntu"
    db.vm.box_url = "C:/me/ubuntu-14.04-amd64.box"
db.vm.hostname = "ubuntu"
    db.vm.network "private_network", ip: "192.168.56.11"
db.vm.provider "virtualbox" do |v|
  v.gui = false
  v.name = "ubuntu-1"
  v.cpus = "1"
  v.memory = "2048"
end
  end
  
  
  
 config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install -y apache2
	 service apache2 start
 SHELL
end