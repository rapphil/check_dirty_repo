# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.


Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  #config.vm.box = "centos/7"
  config.ssh.insert_key = false
  config.vm.provider :libvirt do |libvirt|
    libvirt.memory = 256
    #libvirt.id_ssh_key_file = "/home/rapphil/.ssh/id_rsa"
  end

  def create_machine(vm ,name)
    vm.define name do |machine|
      machine.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/me.pub"
      machine.vm.box = "centos/7"
      machine.vm.hostname = name
    end
  end

  create_machine(config.vm, "my-machine")
end
