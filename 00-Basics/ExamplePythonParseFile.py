import yaml

file = open('test.yml', 'r')

data = file.read()

yml_data = yaml.safe_load(data)

for switch in yml_data:
    print(switch)
    for interface in yml_data[switch]['interfaces']:
        print('interface', interface)
        print('  no switchport')
        print('  ip address', yml_data[switch]['interfaces'][interface]['ipv4'],'/',yml_data[switch]['interfaces'][interface]['mask'])
    print('exit')
    print('router bgp', yml_data[switch]['BGP']['ASN'])

    for neighbor in yml_data[switch]['BGP']['neighbors']:
        print('  neighbor', yml_data[switch]['BGP']['neighbors'][neighbor]["ipv4"], "remote-as", yml_data[switch]['BGP']['neighbors'][neighbor]["ASN"])


        