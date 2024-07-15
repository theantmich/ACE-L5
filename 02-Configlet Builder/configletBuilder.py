################ PYTHON 2 SYNTAX FOR PRINTING STUFF WITH VARIABLES ################
for interfaces in range(10):
    print("interface loopback1%s") % interfaces
    print("  ip address 10.107.%s.1 255.255.255.0") % interfaces


################ PYTHON 3 SYNTAX FOR PRINTING STUFF WITH VARIABLES ################
#for interfaces in range(10):
#    print("interface loopback1%s" % (interfaces))