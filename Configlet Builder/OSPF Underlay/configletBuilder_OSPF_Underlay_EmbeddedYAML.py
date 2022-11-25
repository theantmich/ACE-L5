# coding=utf-8

#Cette section du code permet de lire dynamiquement l'appareil pour lequel crÃ©er le configlet.
#Cela utilise des modules built in CloudVision.
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

#CVP utilise des tags sur les appareils pour dÃ©finir plusieurs Ã©lÃ©ments (hostname, BGP status, MPLS status, Container, etc.)
#Ces tags sont toujours sortis dans une liste en ordre alÃ©atoire, il faut donc faire un match dans la liste puis retourner la valeur correspondant Ã  la clÃ©.

tags = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SYSTEM_LABELS)

for item in tags:
  key = item.split(":")[0]
  if key == "hostname":
    hostname = item.split(":")[1]

#AUTRE MANIÈRE D'AVOIR LE HOSTNAME
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)

#print(hostname)

import yaml #installÃ© dans CloudVision

dataModel = """
DC1:
  spines:
    spine1-DC1:
      Loopback0: "192.168.101.101"
    spine2-DC1:
      Loopback0: "192.168.101.102"
    spine3-DC1:
      Loopback0: "192.168.101.103"
  leafs:
    leaf1-DC1:
      Loopback0: "192.168.101.11"
      Loopback1: "192.168.102.11"
    leaf2-DC1:
      Loopback0: "192.168.101.12"
      Loopback1: "192.168.102.11"
    leaf3-DC1:
      Loopback0: "192.168.101.13"
      Loopback1: "192.168.102.13"
    leaf4-DC1:
      Loopback0: "192.168.101.14"
      Loopback1: "192.168.102.13"
    borderleaf1-DC1:
      Loopback0: "192.168.101.21"
      Loopback1: "192.168.102.21"
    borderleaf2-DC1:
      Loopback0: "192.168.101.22"
      Loopback1: "192.168.102.21"
DC2:
  spines:
    spine1-DC2:
      Loopback0: "192.168.201.101"
    spine2-DC2:
      Loopback0: "192.168.201.102"
    spine3-DC2:
      Loopback0: "192.168.201.103"
  leafs:
    leaf1-DC2:
      Loopback0: "192.168.201.11"
      Loopback1: "192.168.202.11"
    leaf2-DC2:
      Loopback0: "192.168.201.12"
      Loopback1: "192.168.202.11"
    leaf3-DC2:
      Loopback0: "192.168.201.13"
      Loopback1: "192.168.202.13"
    leaf4-DC2:
      Loopback0: "192.168.201.14"
      Loopback1: "192.168.202.13"
    borderleaf1-DC2:
      Loopback0: "192.168.201.21"
      Loopback1: "192.168.202.21"
    borderleaf2-DC2:
      Loopback0: "192.168.201.22"
      Loopback1: "192.168.202.21"
"""

yaml_data = yaml.safe_load(dataModel)

for dc in yaml_data:
  for leaf in yaml_data[dc]['leafs']:
    if leaf == hostname:
      
      mask = "32"
      lo0 = yaml_data[dc]["leafs"][leaf]["Loopback0"]
      lo1 = yaml_data[dc]["leafs"][leaf]["Loopback1"]
      
      print("ip routing ")
      print(" router ospf 100")
      print(" router-id %s") % lo0
      print("!")
      print("interface Loopback0")
      print(" ip address %s/%s") % (lo0,mask)
      print(" ip ospf area 0.0.0.0 ")
      print("!")
      print("interface Loopback1")
      print(" ip address %s/%s") % (lo1,mask)
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
      
  for spine in yaml_data[dc]['spines']:
    if spine == hostname:
      
      mask = "32"
      lo0 = yaml_data[dc]["spines"][spine]["Loopback0"]

      print("ip routing ")
      print(" router ospf 100")
      print(" router-id %s") % lo0
      print("!")
      print("interface Loopback0")
      print(" ip address %s/%s") % (lo0,mask)
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