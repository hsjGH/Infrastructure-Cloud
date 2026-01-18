from ncclient import manager
from ncclient.operations.rpc import RPCError
from xml.dom import minidom

# --- Verbinding maken met de CSR1kv via NETCONF ---
with manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False,
    device_params={'name': 'csr'},  # Belangrijk voor Cisco IOS XE
    look_for_keys=False,
    allow_agent=False,
    timeout=30
) as m:

    print("Connected successfully!\n")

    # --- Part 4: Huidige Native-config ophalen met filter ---
    netconf_filter = """
    <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    </filter>
    """
    netconf_reply = m.get_config(source="running", filter=netconf_filter)
    pretty_xml = minidom.parseString(netconf_reply.xml).toprettyxml()
    print("--- Current Native Configuration ---")
    print(pretty_xml)

    # --- Part 5a: Edit hostname naar NEWHOSTNAME ---
    netconf_hostname = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>NEWHOSTNAME</hostname>
        </native>
    </config>
    """
    netconf_reply_edit = m.edit_config(target="running", config=netconf_hostname)
    print("--- Edit Hostname Reply ---")
    print(minidom.parseString(netconf_reply_edit.xml).toprettyxml())

    # --- Part 5b: Optioneel: hostname terugzetten naar CSR1kv ---
    netconf_hostname_back = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>CSR1kv</hostname>
        </native>
    </config>
    """
    netconf_reply_back = m.edit_config(target="running", config=netconf_hostname_back)
    print("--- Restore Hostname Reply ---")
    print(minidom.parseString(netconf_reply_back.xml).toprettyxml())

    # --- Part 5c: Loopback1 configureren ---
    netconf_loopback1 = """
    <config>
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
       <Loopback>
        <name>1</name>
        <description>My first NETCONF loopback</description>
        <ip>
         <address>
          <primary>
           <address>10.1.1.1</address>
           <mask>255.255.255.0</mask>
          </primary>
         </address>
        </ip>
       </Loopback>
      </interface>
     </native>
    </config>
    """
    netconf_reply_loopback1 = m.edit_config(target="running", config=netconf_loopback1)
    print("--- Create Loopback1 Reply ---")
    print(minidom.parseString(netconf_reply_loopback1.xml).toprettyxml())

    # --- Step 3: Proberen Loopback2 met dezelfde IP (moet fout geven) ---
    netconf_loopback2 = """
    <config>
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
       <Loopback>
        <name>2</name>
        <description>My second NETCONF loopback</description>
        <ip>
         <address>
          <primary>
           <address>10.1.1.1</address>
           <mask>255.255.255.0</mask>
          </primary>
         </address>
        </ip>
       </Loopback>
      </interface>
     </native>
    </config>
    """

    try:
        # Deze zal een RPCError geven vanwege duplicate IP
        netconf_reply_loopback2 = m.edit_config(target="running", config=netconf_loopback2)
        print("--- Create Loopback2 Reply ---")
        print(minidom.parseString(netconf_reply_loopback2.xml).toprettyxml())
    except RPCError as e:
        print("--- Attempt to create Loopback2 failed ---")
        print("RPCError:", e)

    # --- Optioneel: Huidige configuratie opnieuw ophalen om te controleren ---
    netconf_reply_final = m.get_config(source="running", filter=netconf_filter)
    print("--- Final Native Configuration ---")
    print(minidom.parseString(netconf_reply_final.xml).toprettyxml())

print("\nScript execution completed.")
