# coding=utf-8
# Importation des modules extra
import json
import ssl
from cvplibrary import RestClient
import yaml #installÃ© dans CloudVision


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

#Création du socket HTTPS
ssl._create_default_https_context = ssl._create_unverified_context

#Définir le configlet qui a été créé auquel on fera référence comme single source of truth
configlet = "configFile_yaml"

cvp_url = "https://192.168.0.25/cvpservice"

client = RestClient(cvp_url+'/configlet/getConfigletByName.do?name='+configlet,'GET')

if client.connect():
    raw_data = json.loads(client.getResponse())

#Toutes les informations pertinentes de la configuration du configlet sont dans la key "config"
yaml_data = yaml.safe_load(raw_data['config'])

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