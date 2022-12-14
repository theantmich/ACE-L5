import yaml

file = open("OSPF_Loopbacks.yaml",'r')

data = file.read()

ospf_config = yaml.safe_load(data)

for dc in ospf_config:
    print("################",dc,"################")
    for leaf in ospf_config[dc]["Leafs"]:

        print("################",dc,leaf,"################")

        print("ip routing ")
        print(" router ospf 100")
        print(" router-id",ospf_config[dc]["Leafs"][leaf]["Loopback0"])
        print("!")
        print("interface Loopback0")
        print(" ip address",ospf_config[dc]["Leafs"][leaf]["Loopback0"],"/32")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Loopback1")
        print(" ip address",ospf_config[dc]["Leafs"][leaf]["Loopback1"],"/32")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet3")
        print(" description SPINE1 ")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet4")
        print(" description SPINE2 ")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet5")
        print(" description SPINE3 ")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")


    for spine in ospf_config[dc]["Spines"]:

        print("################",dc,spine,"################")

        print("ip routing ")
        print(" router ospf 100")
        print(" router-id",ospf_config[dc]["Spines"][spine]["Loopback0"])
        print("!")
        print("interface Loopback0")
        print(" ip address",ospf_config[dc]["Spines"][spine]["Loopback0"],"/32")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet2")
        print(" description leaf1")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet3")
        print(" description leaf2")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet4")
        print(" description leaf3")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet5")
        print(" description leaf4")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet6")
        print(" description borderleaf1")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")
        print("!")
        print("interface Ethernet7")
        print(" description borderleaf2")
        print(" no switchport")
        print(" ip address unnumbered Loopback0")
        print(" ip ospf network point-to-point ")
        print(" ip ospf area 0.0.0.0 ")