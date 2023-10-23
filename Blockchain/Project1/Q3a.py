from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import HDKey, Key, P2SHAddress
from bitcoinlib.services.services import Service

from lib.config import my_private_key_wif, my_address, faucet_address, network_type

# Definir las constantes manualmente
OP_CHECKMULTISIG = 0xae
OP_PUSHDATA1 = 0x4c

# Generar claves para los clientes
cust1_key = HDKey(network=network_type)
cust2_key = HDKey(network=network_type)
cust3_key = HDKey(network=network_type)

# Crear una dirección multi-sig 2-de-4
bank_key = HDKey(my_private_key_wif)
keys = [bank_key.public_hex, cust1_key.public_hex, cust2_key.public_hex, cust3_key.public_hex]

# Construir el script multisig manualmente
multisig_script = [2] + [OP_PUSHDATA1, len(bank_key.public_byte), bank_key.public_byte, 
                         OP_PUSHDATA1, len(cust1_key.public_byte), cust1_key.public_byte,
                         OP_PUSHDATA1, len(cust2_key.public_byte), cust2_key.public_byte,
                         OP_PUSHDATA1, len(cust3_key.public_byte), cust3_key.public_byte,
                         4, OP_CHECKMULTISIG]

multisig_script_address = P2SHAddress(script=multisig_script, network=network_type).address

def send_to_multisig(amount_to_send, utxo_index):
    # Convertir la cantidad de BTC a satoshis
    amount_to_send_satoshi = int(amount_to_send * 100_000_000)
    
    # Crear una transacción
    t = Transaction(network=network_type)
    
    # Añadir input (UTXO que vamos a gastar)
    t.add_input(utxo_index, keys=[HDKey(my_private_key_wif)])
    
    # Añadir output (destino y cantidad)
    t.add_output(amount_to_send_satoshi, multisig_script_address)
    
    # Firmar la transacción con la clave privada del banco (nosotros)
    t.sign(my_private_key_wif)
    
    # Verificar y enviar la transacción
    if t.verify():
        srv = Service(network=network_type)
        txid = srv.sendrawtransaction(t.raw_hex())
        print(f"Transacción enviada! TXID: {txid}")
    else:
        print("Error al verificar la transacción")

if __name__ == '__main__':
    amount_to_send = 0.001  # En BTC
    utxo_index = 0  # Índice del UTXO que quieres gastar

    send_to_multisig(amount_to_send, utxo_index)
