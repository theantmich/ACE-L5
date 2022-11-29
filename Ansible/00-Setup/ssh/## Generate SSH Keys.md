## Generate SSH Keys

1. ssh-keygen
2. Suivre les prompts (file name, passphrase)
3. cat ssh_key.pub (to paste in the switch CLI)

## Create configuration on switches

1. conf t
2. username <test> privilege 15 role network-admin nopassword
3. username <test> ssh-key <KEY>

## Use SSH Key to login
# Optional : chmod 700 ssh_key

ssh test@192.168.0.21 -i ssh_key