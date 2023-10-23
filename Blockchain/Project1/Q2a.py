from bitcoin.core.script import *
from lib.config import my_private_key, my_address, faucet_address, network_type
from Q1 import send_to_faucet
from docs.transactions import Q2a_txid

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# Assuming a standard P2PKH scriptPubKey
Q2a_txout_scriptPubKey = [
    OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = Q2a_txid
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    # Use the send_to_faucet function from Q1.py
    send_to_faucet(amount_to_send, utxo_index)
