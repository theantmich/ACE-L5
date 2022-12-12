import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames

tags = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SYSTEM_LABELS)

for item in tags:
  key = item.split(":")[0]
  if key == "hostname":
    hostname = item.split(":")[1]

yaml_data = """
spine1-DC1:
    Loopback0: 192.168.101.101
spine2-DC1:
    Loopback0: 192.168.101.102
spine3-DC1:
    Loopback0: 192.168.101.103
leaf1-DC1:
    Loopback0: 192.168.101.11
    Loopback1: 192.168.102.11
leaf2-DC1:
    Loopback0: 192.168.101.12
    Loopback1: 192.168.102.11
leaf3-DC1:
    Loopback0: 192.168.101.13
    Loopback1: 192.168.102.13
leaf4-DC1:
    Loopback0: 192.168.101.14
    Loopback1: 192.168.102.13
borderleaf1-DC1:
    Loopback0: 192.168.101.21
    Loopback1: 192.168.102.21
borderleaf2-DC1:
    Loopback0: 192.168.101.22
    Loopback1: 192.168.102.21
spine1-DC2:
    Loopback0: 192.168.201.101
spine2-DC2:
    Loopback0: 192.168.201.102
spine3-DC2:
   Loopback0: 192.168.201.103
leaf1-DC2:
    Loopback0: 192.168.201.11
    Loopback1: 192.168.202.11
leaf2-DC2:
    Loopback0: 192.168.201.12
    Loopback1: 192.168.202.11
leaf3-DC2:
    Loopback0: 192.168.201.13
    Loopback1: 192.168.202.13
leaf4-DC2:
    Loopback0: 192.168.201.14
    Loopback1: 192.168.202.13
borderleaf1-DC2:
    Loopback0: 192.168.201.21
    Loopback1: 192.168.202.21
borderleaf2-DC2:
    Loopback0: 192.168.201.22
    Loopback1: 192.168.202.21
"""

config = yaml.safe_load(yaml_data)

if "leaf" in hostname:
  lo1 = config[hostname]["Loopback1"]
  print("interface Loopback1")
  print(" ip address %s/32") % lo1  
  
lo0 = config[hostname]["Loopback0"]
print("interface Loopback0")
print(" ip address %s/32") % lo0

