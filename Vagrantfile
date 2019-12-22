# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "fatboy.skynet.lan"
  config.vm.network "private_network", ip: "192.168.99.10"
  config.vm.synced_folder ".", "/ansible", mount_options: ["dmode=755,fmode=644"]
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = 2048
    vb.cpus = 2
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end

  config.vbguest.auto_update = false

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3-pip
    pip3 install git+https://github.com/ansible/ansible.git@devel
    ansible --version
  SHELL
end
