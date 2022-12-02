# Verify if the collection is installed
ansible-galaxy collection list | grep arista

# Install the CVP collection
ansible-galaxy collection install arista.cvp:==3.3.0