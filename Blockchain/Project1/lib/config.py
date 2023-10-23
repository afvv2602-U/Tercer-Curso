from bitcoinlib.keys import HDKey, Address

# Configuramos para usar testnet en bitcoinlib
network_type = 'testnet'

faucet_address = Address('mgd5EmL1xvKCx2C3nPrpi1ps7gbp4raNCb', network=network_type)

######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key_wif = 'tprv8jfAS6FgmzpbvPtPcfqR8Y8p7KheFCPjcChCrmYAkWkUF4KvvUFkCkPCocuGuRGA2RkJthFLWQErf9YLD8YSFFz1ykFnBGhf1gUwfyt2Tri'

# Convert the HD private key to an HDKey object and get the associated address
key = HDKey(my_private_key_wif, network=network_type)
my_private_key = key.wif()
my_address = key.address()
######################################################################
