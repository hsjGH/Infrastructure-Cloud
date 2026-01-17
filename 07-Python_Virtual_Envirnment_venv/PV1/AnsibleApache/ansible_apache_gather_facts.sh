#!/bin/bash

# Show IPv4 address
echo '----'
echo "IPV4 ADDRESS"
ip addr | grep "inet " | cut -d' ' -f6
echo '----'

# Show Ansible config file
echo "ANSIBLE CONFIG FILE"
cat ansible.cfg
echo '----'

# Check Ansible version
echo "ANSIBLE VERSION"
ansible --version
echo '----'

# Check inventory hosts
echo "ANSIBLE INVENTORY"
ansible all --list-hosts
echo '----'

# Ping test to all hosts
echo "ANSIBLE PING TEST"
ansible all -m ping
echo '----'
