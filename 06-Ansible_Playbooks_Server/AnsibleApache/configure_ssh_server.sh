# install ssh server
sudo apt-get install openssh-server

# install sshpass utility
sudo apt-get install sshpass

# enable ssh server
sudo sytemctl start ssh

# check if ansible is running
echo "ansible --version"