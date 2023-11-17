from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import HDKey, Key, Address
from bitcoinlib.services.services import Service

# Importar configuraciones y transacciones
from lib.config import my_private_key_wif, my_address, faucet_address, network_type
from docs.transactions import Q1_txid

def send_to_faucet(amount_to_send, utxo_index):
    # Convertir la cantidad de BTC a satoshis
    amount_to_send_satoshi = int(amount_to_send * 100_000_000)
    
    # Crear una transacción
    t = Transaction(network=network_type)
    
    # Añadir input (UTXO que vamos a gastar)
    t.add_input(Q1_txid, utxo_index, keys=[HDKey(my_private_key_wif)])
    
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

# Ejemplo de uso
# Estos valores son solo ejemplos y deben ser reemplazados por los valores reales
amount_to_send = 0.001  # En BTC
utxo_index = 0  # Índice del UTXO que quieres gastar

send_to_faucet(amount_to_send, utxo_index)
