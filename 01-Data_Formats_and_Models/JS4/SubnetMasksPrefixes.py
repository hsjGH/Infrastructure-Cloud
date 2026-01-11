import json

# Mapping van subnet mask naar CIDR prefix
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
    """
    Zet een subnetmask om naar CIDR prefix.
    """
    try:
        return netmask_prefixes[p_subnet_mask]
    except KeyError:
        return None


# Input en basis output
subnet_input = input('Wat is je subnet mask? ')
net_prefix = get_net_prefix(subnet_input)

if net_prefix is None:
    print("Ongeldig subnet mask")
else:
    print(f"Je prefix is: {net_prefix}")


# JSON conversie (experiment: dict <-> JSON string)
netmask_pref_str = json.dumps(netmask_prefixes)   # dict → JSON string
netmask_pref_dict = json.loads(netmask_pref_str)  # JSON string → dict

print(type(netmask_pref_str))
print(type(netmask_pref_dict))


def get_number_ip_addresses(p_prefix):
    """
    Berekent het totaal aantal IP-adressen op basis van CIDR prefix.
    """
    if not p_prefix.startswith('/'):
        return None
    pbits = 32 - int(p_prefix[1:])
    return 2 ** pbits


def get_number_ip_hosts(p_prefix):
    """
    Berekent het aantal bruikbare hosts (exclusief network & broadcast).
    """
    total = get_number_ip_addresses(p_prefix)
    if total is None or total < 2:
        return None
    return total - 2


# Test
print(get_number_ip_addresses('/24'))   # 256
print(get_number_ip_hosts('/24'))       # 254
