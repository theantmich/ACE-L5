# coding=utf-8

#Cette section du code permet de lire dynamiquement l'appareil pour lequel créer le configlet.
#Cela utilise des modules built in CloudVision.
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

#CVP utilise des tags sur les appareils pour définir plusieurs éléments (hostname, BGP status, MPLS status, Container, etc.)
#Ces tags sont toujours sortis dans une liste en ordre aléatoire, il faut donc faire un match dans la liste puis retourner la valeur correspondant à la clé.

tags = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SYSTEM_LABELS)

for item in tags:
  key = item.split(":")[0]
  if key == "hostname":
    hostname = item.split(":")[1]

print(hostname)

import yaml #installé dans CloudVision

dataModel = """
leaf1-dc1:
  interfaces:
    Ethernet1:
      ipv4: "192.168.1.1"
      mask: "24"
    Ethernet2:
      ipv4: "192.168.2.1"
      mask: "24"
    Ethernet3:
      ipv4: "192.168.3.1"
      mask: "24"
  BGP:
    ASN: "65101"
    neighbors:
      neighbor1: 
        ipv4: "192.168.11.1"
        ASN:  "65102"
      neighbor2: 
        ipv4: "192.168.12.1"
        ASN: "65102"

leaf1-dc2:
  interfaces:
    Ethernet1:
      ipv4: "192.168.11.1"
      mask: "24"
    Ethernet2:
      ipv4: "192.168.12.1"
      mask: "24"
    Ethernet3:
      ipv4: "192.168.13.1"
      mask: "24"
  BGP:
    ASN: "65102"
    neighbors:
      neighbor1: 
        ipv4: "192.168.1.1"
        ASN:  "65102"
      neighbor2: 
        ipv4: "192.168.2.1"
        ASN: "65102"
"""

yaml_data = yaml.safe_load(dataModel)

print(yaml_data)
for interface in yaml_data