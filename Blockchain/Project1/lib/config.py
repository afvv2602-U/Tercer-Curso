from bitcoinlib.keys import HDKey, Address

# Configuramos para usar testnet en bitcoinlib
network_type = 'testnet'

faucet_address = Address('myuAFy5MxZpmfUfc8pGmdy7eLMMjX5rzju', network=network_type)

######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key_wif = 'tprv8jBbr7HRyWRvHgLGwLWYurbozkhvzdXdoLCe4A7P9gjVa6SHwCCibZDuDGZ75RkmiU5E9xboKW5HttapPGqXEXvkzZq2CCHEPZ9A8PesLvB'

# Convert the HD private key to an HDKey object and get the associated address
key = HDKey(my_private_key_wif, network=network_type)
my_private_key = key.wif()
my_address = key.address()
######################################################################
