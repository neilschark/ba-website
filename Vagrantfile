Vagrant.configure("2") do |config|
    #************************************************************************
    # Classic
    #************************************************************************
    # Backend
    #config.vm.define "multi_backend_classic" do |backend|
    #  backend.vm.provider "virtualbox" do |v|
    #    v.name = "multi_backend_classic"
    #  end
    #  backend.vm.provision :shell, path: "vm_configs/classic/classic.sh"
    #  backend.vm.provision :shell, path: "vm_configs/classic/backend.sh"
    #end
#
    ## Frontend
    #config.vm.define "multi_frontend_classic" do |frontend|
    #  frontend.vm.provider "virtualbox" do |v|
    #    v.name = "multi_frontend_classic"
    #  end
    #  frontend.vm.provision :shell, path: "vm_configs/classic/classic.sh"
    #  frontend.vm.provision :shell, path: "vm_configs/classic/frontend.sh"
    #end
#
    ## DB
    #config.vm.define "multi_db_classic" do |db|
    #  db.vm.provider "virtualbox" do |v|
    #    v.name = "multi_db_classic"
    #  end
    #  db.vm.provision :shell, path: "vm_configs/classic/classic.sh"
    #  db.vm.provision :shell, path: "vm_configs/classic/db.sh"
    #end
    # Single VM
    config.vm.define "single_vm_classic" do |single|
      single.vm.provider "virtualbox" do |v|
        v.name = "single_vm_classic"
      end
      single.vm.provision :shell, reboot: true, path: "vm_configs/classic/classic.sh"
      single.vm.provision :shell, reboot: true, path: "vm_configs/classic/single.sh"
      single.vm.network "public_network", bridge: "enp7s0", ip: "192.168.69.210"
    end


    #************************************************************************
    # Docker
    #************************************************************************

    #config.vm.define "multi_backend_docker" do |backend|
    #  backend.vm.provider "virtualbox" do |v|
    #    v.name = "multi_backend_docker"
    #  end
    #  backend.vm.provision :shell, path: "vm_configs/docker/docker.sh"
    #  backend.vm.provision :shell, path: "vm_configs/docker/docker2.sh"
    #  #backend.vm.provision :shell, path: "backend.sh"
    #end
#
    ## Frontend
    #config.vm.define "multi_frontend_docker" do |frontend|
    #  frontend.vm.provider "virtualbox" do |v|
    #    v.name = "multi_frontend_docker"
    #  end
    #  frontend.vm.provision :shell, path: "vm_configs/docker/docker.sh"
    #  frontend.vm.provision :shell, path: "vm_configs/docker/docker2.sh"
    #  #frontend.vm.provision :shell, path: "frontend.sh"
    #end
#
    ## DB
    #config.vm.define "multi_db_docker" do |db|
    #  db.vm.provider "virtualbox" do |v|
    #    v.name = "multi_db_docker"
    #  end
    #  db.vm.provision :shell, path: "vm_configs/docker/docker.sh"
    #  db.vm.provision :shell, path: "vm_configs/docker/docker2.sh"
    #  #db.vm.provision :shell, path: "db.sh"
    #end

    # Single VM
    config.vm.define "single_vm_docker" do |single|
      single.vm.provider "virtualbox" do |v|
        v.name = "single_vm_docker"
      end
      single.vm.provision :shell, reboot: true, path: "vm_configs/docker/docker.sh"
      single.vm.provision :shell, path: "vm_configs/docker/docker2.sh"
      single.vm.network "public_network", bridge: "enp7s0", ip: "192.168.69.211"
      #single.vm.provision :shell, path: "single.sh"
    end

    #************************************************************************
    # container-orchestration
    #************************************************************************
    # Backend
    #config.vm.define "multi_backend_orchestration" do |backend|
    #  backend.vm.provider "virtualbox" do |v|
    #    v.name = "multi_backend_orchestration"
    #  end
    #  backend.vm.provision :shell, path: "vm_configs/orchestration/orchestration.sh"
    #  #backend.vm.provision :shell, path: "vm_configs/classic/backend.sh"
    #end
#
    ## Frontend
    #config.vm.define "multi_frontend_orchestration" do |frontend|
    #  frontend.vm.provider "virtualbox" do |v|
    #    v.name = "multi_frontend_orchestration"
    #  end
    #  frontend.vm.provision :shell, path: "vm_configs/orchestration/orchestration.sh"
    #  #frontend.vm.provision :shell, path: "vm_configs/classic/frontend.sh"
    #end
#
    ## DB
    #config.vm.define "multi_db_orchestration" do |db|
    #  db.vm.provider "virtualbox" do |v|
    #    v.name = "multi_db_orchestration"
    #  end
    #  db.vm.provision :shell, path: "vm_configs/orchestration/orchestration.sh"
    #  #db.vm.provision :shell, path: "vm_configs/classic/db.sh"
    #end

    # Single VM
    config.vm.define "single_vm_orchestration" do |single|
      single.vm.provider "virtualbox" do |v|
        v.name = "single_vm_orchestration"
      end
      single.vm.provision :shell, reboot: true, path: "vm_configs/orchestration/orchestration.sh"
      single.vm.network "public_network", bridge: "enp7s0", ip: "192.168.69.212"
      #single.vm.provision :shell, path: "vm_configs/classic/single.sh"
    end

    # Config for all machines
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
    end
    config.vm.box = "debian/buster64"
    #config.vm.network "public_network", bridge: "enp7s0"
      
  end