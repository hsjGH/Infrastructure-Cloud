netmask_prefixes = {
    '255.255.255.255': '/32',
    '255.255.255.254': '/31',
    '255.255.255.252': '/30',
    '255.255.255.248': '/29',
    '255.255.255.240': '/28',
    '255.255.255.224': '/27',
    '255.255.255.192': '/26',
    '255.255.255.128': '/25',
    '255.255.255.0':   '/24',
    '255.255.254.0':   '/23',
    '255.255.252.0':   '/22',
    '255.255.248.0':   '/21',
    '255.255.240.0':   '/20',
    '255.255.224.0':   '/19',
    '255.255.192.0':   '/18',
    '255.255.128.0':   '/17',
    '255.255.0.0':     '/16',
    '255.254.0.0':     '/15',
    '255.252.0.0':     '/14',
    '255.248.0.0':     '/13',
    '255.240.0.0':     '/12',
    '255.224.0.0':     '/11',
    '255.192.0.0':     '/10',
    '255.128.0.0':     '/9',
    '255.0.0.0':       '/8'
}

def get_net_prefix(p_subnet_mask):
    try: 
        net_prefix = netmask_prefixes[p_subnet_mask]
        return net_prefix
    except KeyError:
        return "Wrong input: garbage in, garbage out"

# Dev test function
subnet_input = input('Wat is je subnet mask? ')
net_prefix = get_net_prefix(subnet_input)
print(f"Je Prefix is: {net_prefix}")



import json
print(type(net_prefix))
print(type(netmask_prefixes))

# Maak van een dict een string
netmask_pref_str = json.dumps(netmask_prefixes)
print(type(netmask_pref_str))
# Maak van een string een dict
netmask_pref_dict = json.loads(netmask_pref_str)
print(type(netmask_pref_str))



def get_number_ip_addresses(p_prefix):
    pbits = 32-int(p_prefix[1:])
    return 2 ** pbits

def get_number_ip_hosts(p_prefix):
    pbits = get_number_ip_addresses(p_prefix)
    return pbits - 2

# dev test function
net_number_addr = get_number_ip_addresses('/24')
net_number_ip_hosts = get_number_ip_hosts('/24')
print(net_number_addr)
print(net_number_ip_hosts)
