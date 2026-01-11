# show ipv4 address
echo '----'
echo "IPV4 ADDRESS"
ip addr | grep "inet " | cut -d' ' -f6
echo '----'
# show ansible config file
echo "ANSIBLE CONFIG FILE"
cat ansible.cfg
echo '----'
# check ansible version 
