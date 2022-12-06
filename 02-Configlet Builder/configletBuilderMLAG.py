from cvplibrary import CVPGlobalVariables, GlobalVariableNames

#CVP utilise des tags sur les appareils pour définir plusieurs éléments (hostname, BGP status, MPLS status, Container, etc.)
#Ces tags sont toujours sortis dans une liste en ordre aléatoire, il faut donc faire un match dans la liste puis retourner la valeur correspondant à la clé.

tags = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SYSTEM_LABELS)

for item in tags:
  key = item.split(":")[0]
  if key == "hostname":
    hostname = item.split(":")[1]

#print(hostname)

import yaml #installé dans CloudVision

# dataModel = """
# leaf1-DC1 : Odd
# leaf2-DC1 : Even
# """

#yaml_data = yaml.safe_load(dataModel)

if 'borderleaf' in hostname:
    mlag_id = hostname[10]
elif 'leaf' in hostname:
    mlag_id = hostname[4]

if int(mlag_id) % 2 == 0:
    mlag_type = "Even"

    print("spanning-tree mode mstp ")
    print("no spanning-tree vlan-id 4094 ")
    print("vlan 4094")
    print("trunk group MLAGPEER ")
    print("interface Vlan4094")
    print("description MLAG PEER LINK ")
    print("ip address 192.168.255.2/30")
    print("interface Port-Channel10")
    print("description MLAG PEER LINK - LEAF")
    print("switchport mode trunk")
    print("switchport trunk group MLAGPEER  ")
    print("mlag configuration")
    print("domain-id MLAG ")
    print("local-interface Vlan4094")
    print("peer-address 192.168.255.1 ")
    print("peer-link Port-Channel10")
    print("interface Ethernet1  ")
    print("description MLAG PEER LINK - LEAF")
    print("switchport mode trunk")
    print("channel-group 10 mode active  ")
    print("interface Ethernet2  ")
    print("description MLAG PEER LINK -- LEAF  ")
    print("switchport mode trunk")
    print("channel-group 10 mode active  ")

elif int(mlag_id) % 2 == 1:
    mlag_type = "Odd"

    print("spanning-tree mode mstp ")
    print("no spanning-tree vlan-id 4094 ")
    print("vlan 4094")
    print("trunk group MLAGPEER ")
    print("interface Vlan4094")
    print("description MLAG PEER LINK ")
    print("ip address 192.168.255.1/30")
    print("interface Port-Channel10")
    print("description MLAG PEER LINK - LEAF")
    print("switchport mode trunk")
    print("switchport trunk group MLAGPEER  ")
    print("mlag configuration")
    print("domain-id MLAG ")
    print("local-interface Vlan4094")
    print("peer-address 192.168.255.2 ")
    print("peer-link Port-Channel10")
    print("interface Ethernet1  ")
    print("description MLAG PEER LINK - LEAF")
    print("switchport mode trunk")
    print("channel-group 10 mode active  ")
    print("interface Ethernet2  ")
    print("description MLAG PEER LINK -- LEAF  ")
    print("switchport mode trunk")
    print("channel-group 10 mode active  ")
												