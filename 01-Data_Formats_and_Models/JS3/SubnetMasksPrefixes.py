import json

# Dictionary dat IPv4 subnet masks mapt naar CIDR-prefixen
# Dit wordt vaak gebruikt in netwerkautomatisatie om legacy masks
# om te zetten naar CIDR-notatie
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
    Zet een subnet mask om naar CIDR-prefix.
    Indien het subnet mask niet bestaat in de mapping,
    wordt een foutmelding teruggegeven.
    """
    try:
        return netmask_prefixes[p_subnet_mask]
    except KeyError:
        return "Invalid subnet mask"

# Test: gebruiker geeft subnet mask in
subnet_input = input('Wat is je subnet mask? ')
net_prefix = get_net_prefix(subnet_input)
print(f"Je prefix is: {net_prefix}")

# Controle van datatypes (dict vs string)
print(type(net_prefix))
print(type(netmask_prefixes))

# Conversie van dictionary naar JSON-string
netmask_pref_str = json.dumps(netmask_prefixes)
print(type(netmask_pref_str))

# Conversie van JSON-string terug naar dictionary
netmask_pref_dict = json.loads(netmask_pref_str)
print(type(netmask_pref_dict))

def get_number_ip_addresses(p_prefix):
    """
    Berekent het totaal aantal IP-adressen in een subnet
    op basis van het CIDR-prefix.
    """
    host_bits = 32 - int(p_prefix[1:])
    return 2 ** host_bits

def get_number_ip_hosts(p_prefix):
    """
    Berekent het aantal bruikbare hosts in een subnet.
    Netacad-regel: netwerkadres en broadcastadres worden afgetrokken.
    """
    total_addresses = get_number_ip_addresses(p_prefix)
    return total_addresses - 2

# Test met een klassiek /24 netwerk
net_number_addr = get_number_ip_addresses('/24')
net_number_ip_hosts = get_number_ip_hosts('/24')

print(net_number_addr)
print(net_number_ip_hosts)
