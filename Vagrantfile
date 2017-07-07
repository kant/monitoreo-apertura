VAGRANTFILE_API_VERSION = "2"

SSH_KEYS = [ '~/.vagrant.d/insecure_private_key', '~/.ssh/id_rsa']


application_name = "monitoreo"
checkout_branch = "master"
database_user = "monitoreo_db_user"
database_password = "monitoreo_db_pass"

repo_url = "git@github.com:datosgobar/monitoreo-apertura.git"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.ssh.private_key_path = SSH_KEYS
  config.ssh.forward_agent = true
  config.ssh.insert_key = false
  config.vm.define "webserver" do |web|
      web.ssh.private_key_path = SSH_KEYS
      web.ssh.forward_agent = true
      web.ssh.insert_key = false
      web.vm.network "private_network", ip: "192.168.33.10"
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deploy/site.yml"
    ansible.groups = {
        "webservers" => ["webserver"]
    }
    ansible.verbose = "vvv"
    #ansible.tags = ["quickly"]
    ansible.extra_vars = {
        "application_clone_url" => repo_url,
        "postgresql_user" => database_user,
        "postgresql_password" => database_password,
        "checkout_branch" => checkout_branch,
        "ansible_ssh_user" => "vagrant",
    }
  end
end