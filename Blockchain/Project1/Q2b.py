from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import HDKey, Key, Address
from bitcoinlib.services.services import Service
from bitcoinlib.scripts import Script

from lib.config import my_private_key_wif, my_address, faucet_address, network_type
from docs.transactions import Q2a_txid

def send_to_faucet_with_custom_scriptSig(amount_to_send, utxo_index, scriptSig):
    # Convertir la cantidad de BTC a satoshis
    amount_to_send_satoshi = int(amount_to_send * 100_000_000)
    
    # Crear una transacción
    t = Transaction(network=network_type)
    
    # Añadir input (UTXO que vamos a gastar) con el unlocking_script
    t.add_input(Q2a_txid, utxo_index, unlocking_script=scriptSig)
    
    # Añadir output (destino y cantidad)
    t.add_output(amount_to_send_satoshi, faucet_address)
    
    # Convertir la clave privada WIF extendida a un objeto HDKey y obtener la clave privada en formato hexadecimal
    hdkey_obj = HDKey(my_private_key_wif)
    private_key_hex = hdkey_obj.private_hex
    
    # Convertir la clave privada hexadecimal a un objeto Key
    key_obj = Key(private_key_hex)
    
    # Firmar la transacción con el objeto Key
    t.sign(key_obj)
    
    # Verificar y enviar la transacción
    if t.verify():
        srv = Service(network=network_type)
        txid = srv.sendrawtransaction(t.raw_hex())
        print(f"Transacción enviada! TXID: {txid}")
    else:
        print("Error al verificar la transacción")

if __name__ == '__main__':
    amount_to_send = 0.001  # En BTC
    utxo_index = 2 # Índice del UTXO que quieres gastar

    # Supongamos que x e y son los dos números enteros que quieres usar
    x = 123
    y = 456

    # Convertimos x e y a bytes
    x_bytes = x.to_bytes((x.bit_length() + 7) // 8, 'big')
    y_bytes = y.to_bytes((y.bit_length() + 7) // 8, 'big')

    # Creamos el script
    unlocking_script = Script([len(x_bytes), x_bytes, len(y_bytes), y_bytes])

    # Convertimos el script a bytes
    unlocking_script_bytes = unlocking_script.raw

    send_to_faucet_with_custom_scriptSig(amount_to_send, utxo_index, unlocking_script_bytes)
