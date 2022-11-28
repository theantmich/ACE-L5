import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)

yaml_data = """
spine1-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.101"
            mask: "32"
        Ethernet2: 
            ipv4: "192.168.103.1"
            mask: "31"
        Ethernet3: 
            ipv4: "192.168.103.7"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.13"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.19"
            mask: "31"
        Ethernet6: 
            ipv4: "192.168.103.25"
            mask: "31"
        Ethernet7: 
            ipv4: "192.168.103.31"
            mask: "31"                    
    BGP:
        ASN: "65100"

spine2-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.102"
            mask: "32"
        Ethernet2: 
            ipv4: "192.168.103.3"
            mask: "31"
        Ethernet3: 
            ipv4: "192.168.103.9"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.15"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.21"
            mask: "31"
        Ethernet6: 
            ipv4: "192.168.103.27"
            mask: "31"
        Ethernet7: 
            ipv4: "192.168.103.33"
            mask: "31"    
    BGP:
        ASN: "65100"

spine3-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.103"
            mask: "32"
        Ethernet2: 
            ipv4: "192.168.103.5"
            mask: "31"
        Ethernet3: 
            ipv4: "192.168.103.11"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.17"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.23"
            mask: "31"
        Ethernet6: 
            ipv4: "192.168.103.29"
            mask: "31"
        Ethernet7: 
            ipv4: "192.168.103.35"
            mask: "31"    
    BGP:
        ASN: "65100"

leaf1-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.11"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.102.11"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.103.0"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.2"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.4"
            mask: "31"
    BGP:
        ASN: "65101"
        spine-peers: 
            peer1: "192.168.103.1"
            peer2: "192.168.103.3"
            peer3: "192.168.103.5"
    mlag_peer: "leaf2-DC1"
leaf2-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.12"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.102.11"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.103.6"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.8"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.10"
            mask: "31"
    BGP:
        ASN: "65101"
        spine-peers: 
            peer1: "192.168.103.7"
            peer2: "192.168.103.9"
            peer3: "192.168.103.11"
    mlag_peer: "leaf1-DC1"    
leaf3-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.13"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.102.13"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.103.12"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.14"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.16"
            mask: "31"
    BGP:
        ASN: "65102"
        spine-peers: 
            peer1: "192.168.103.13"
            peer2: "192.168.103.15"
            peer3: "192.168.103.17"
    mlag_peer: "leaf4-DC1"
leaf4-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.14"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.102.12"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.103.18"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.20"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.22"
            mask: "31"
    BGP:
        ASN: "65102"
        spine-peers: 
            peer1: "192.168.103.19"
            peer2: "192.168.103.21"
            peer3: "192.168.103.23"
    mlag_peer: "leaf3-DC1"
borderleaf1-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.21"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.102.21"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.103.24"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.26"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.28"
            mask: "31"
        Ethernet12: 
            ipv4: "192.168.254.0"
            mask: "31"
    BGP:
        ASN: "65103"
        spine-peers: 
            peer1: "192.168.103.25"
            peer2: "192.168.103.27"
            peer3: "192.168.103.29"
    mlag_peer: "borderleaf2-DC1"
borderleaf2-DC1:
    interfaces:
        Loopback0:
            ipv4: "192.168.101.22"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.102.21"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.103.30"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.103.32"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.103.34"
            mask: "31"
        Ethernet12: 
            ipv4: "192.168.254.2"
            mask: "31"
    BGP:
        ASN: "65103"
        spine-peers: 
            peer1: "192.168.103.31"
            peer2: "192.168.103.33"
            peer3: "192.168.103.35"
    mlag_peer: "borderleaf1-DC1"
spine1-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.101"
            mask: "32"
        Ethernet2: 
            ipv4: "192.168.203.1"
            mask: "31"
        Ethernet3: 
            ipv4: "192.168.203.7"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.13"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.19"
            mask: "31"
        Ethernet6: 
            ipv4: "192.168.203.25"
            mask: "31"
        Ethernet7: 
            ipv4: "192.168.203.31"
            mask: "31"                    
    BGP:
        ASN: "65200"

spine2-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.102"
            mask: "32"
        Ethernet2: 
            ipv4: "192.168.203.3"
            mask: "31"
        Ethernet3: 
            ipv4: "192.168.203.9"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.15"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.21"
            mask: "31"
        Ethernet6: 
            ipv4: "192.168.203.27"
            mask: "31"
        Ethernet7: 
            ipv4: "192.168.203.33"
            mask: "31"    
    BGP:
        ASN: "65200"

spine3-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.103"
            mask: "32"
        Ethernet2: 
            ipv4: "192.168.203.5"
            mask: "31"
        Ethernet3: 
            ipv4: "192.168.203.11"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.17"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.23"
            mask: "31"
        Ethernet6: 
            ipv4: "192.168.203.29"
            mask: "31"
        Ethernet7: 
            ipv4: "192.168.203.35"
            mask: "31"    
    BGP:
        ASN: "65200"

leaf1-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.11"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.202.11"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.203.0"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.2"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.4"
            mask: "31"
    BGP:
        ASN: "65201"
        spine-peers: 
            peer1: "192.168.203.1"
            peer2: "192.168.203.3"
            peer3: "192.168.203.5"
    mlag_peer: "leaf2-DC2"
leaf2-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.12"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.202.11"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.203.6"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.8"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.10"
            mask: "31"
    BGP:
        ASN: "65201"
        spine-peers: 
            peer1: "192.168.203.7"
            peer2: "192.168.203.9"
            peer3: "192.168.203.11"
    mlag_peer: "leaf1-DC2"        
leaf3-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.13"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.202.13"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.203.12"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.14"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.16"
            mask: "31"
    BGP:
        ASN: "65202"
        spine-peers: 
            peer1: "192.168.203.13"
            peer2: "192.168.203.15"
            peer3: "192.168.203.17"
    mlag_peer: "leaf4-DC2"
leaf4-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.14"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.202.12"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.203.18"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.20"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.22"
            mask: "31"
    BGP:
        ASN: "65202"
        spine-peers: 
            peer1: "192.168.203.19"
            peer2: "192.168.203.21"
            peer3: "192.168.203.23"
    mlag_peer: "leaf3-DC2"
borderleaf1-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.21"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.202.21"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.203.24"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.26"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.28"
            mask: "31"
        Ethernet12: 
            ipv4: "192.168.254.4"
            mask: "31"
    BGP:
        ASN: "65203"
        spine-peers: 
            peer1: "192.168.203.25"
            peer2: "192.168.203.27"
            peer3: "192.168.203.29"
    mlag_peer: "borderleaf2-DC2"
borderleaf2-DC2:
    interfaces:
        Loopback0:
            ipv4: "192.168.201.22"
            mask: "32"
        Loopback1: 
            ipv4: "192.168.202.21"
            mask: "32"
        Ethernet3: 
            ipv4: "192.168.203.30"
            mask: "31"
        Ethernet4: 
            ipv4: "192.168.203.32"
            mask: "31"
        Ethernet5: 
            ipv4: "192.168.203.34"
            mask: "31"
        Ethernet12: 
            ipv4: "192.168.254.6"
            mask: "31"
    BGP:
        ASN: "65203"
        spine-peers: 
            peer1: "192.168.203.31"
            peer2: "192.168.203.33"
            peer3: "192.168.203.35"
    mlag_peer: "borderleaf1-DC2"
"""

config = yaml.safe_load(yaml_data)

def configure_interfaces():
  for interface in config[hostname]["interfaces"]:
    
    ip = config[hostname]["interfaces"][interface]["ipv4"]
    mask = config[hostname]["interfaces"][interface]["mask"]
  
    print("interface %s") % interface
    if "Ethernet" in interface:
      print(" no switchport")
    print(" ip address %s/%s") % (ip,mask)

def configure_bgp():
  print("ip prefix-list LOOPBACK")
  print(" seq 10 permit 192.168.101.0/24 ge 24")
  print(" seq 20 permit 192.168.102.0/24 ge 24")
  print(" seq 30 permit 192.168.201.0/24 ge 24")
  print(" seq 40 permit 192.168.202.0/24 ge 24")
  print("route-map LOOPBACK permit 10")
  print(" match ip address prefix-list LOOPBACK")
  
  if "spine" in hostname:
    print("peer-filter LEAF-AS-RANGE")
    print("  10 match as-range 65000-65535 result accept")
    
    for switch in config:
      ASN = config[hostname]["BGP"]["ASN"]
      lo0 = config[hostname]["interfaces"]["Loopback0"]["ipv4"]
      
      print("router bgp %s") % ASN
      print(" router-id %s") % lo0
      
      print("  no bgp default ipv4-unicast")
      print("  maximum-paths 3")
      print("  distance bgp 20 200 200")
      print("  bgp listen range 192.168.0.0/16 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE")
      print("  neighbor LEAF_Underlay peer group")
      print("  neighbor LEAF_Underlay send-community")
      print("  neighbor LEAF_Underlay maximum-routes 12000")
      print("  redistribute connected route-map LOOPBACK")
      print("  address-family ipv4")
      print("    neighbor LEAF_Underlay activate")
      print("    redistribute connected route-map LOOPBACK")
      
  if "leaf" in hostname:
    ASN = config[hostname]["BGP"]["ASN"]
    lo0 = config[hostname]["interfaces"]["Loopback0"]["ipv4"]
    
    print("router bgp %s") % ASN
    print(" router-id %s") % lo0
    print("  no bgp default ipv4-unicast")
    print("  maximum-paths 3")
    print("  distance bgp 20 200 200")
    print("  neighbor SPINE_Underlay peer group")
    
    if "DC1" in hostname:
      spineASN = config["spine1-DC1"]["BGP"]["ASN"]
    elif "DC2" in hostname:
      spineASN = config["spine1-DC2"]["BGP"]["ASN"]

    print("  neighbor SPINE_Underlay remote-as %s") % spineASN
    print("  neighbor SPINE_Underlay send-community")
    print("  neighbor SPINE_Underlay maximum-routes 12000")
    print("  neighbor LEAF_Peer peer group")
    
    mlag_peer = config[hostname]["mlag_peer"]
    mlag_peer_ASN = config[mlag_peer]["BGP"]["ASN"]
    mlag_peer_ip = config[mlag_peer]["interfaces"]["Loopback0"]["ipv4"]
    
    print("  neighbor LEAF_Peer remote-as %s") % mlag_peer_ASN
    print("  neighbor LEAF_Peer next-hop-self")
    print("  neighbor LEAF_Peer maximum-routes 12000")

# List the neighbor IPs here. It should be three spines for SPINE_Underlay and one LEAF_Peer
    for peer in config[hostname]["BGP"]["spine-peers"]:
      peer_ip = config[hostname]["BGP"]["spine-peers"][peer]
      print("  neighbor %s peer group SPINE_Underlay") % peer_ip
    
    print("  neighbor %s peer group LEAF_Peer") % mlag_peer_ip
    print("  redistribute connected route-map LOOPBACK")
    print("  address-family ipv4")
    print("    neighbor SPINE_Underlay activate")
    print("    neighbor LEAF_Peer activate")

configure_interfaces()
configure_bgp()
    