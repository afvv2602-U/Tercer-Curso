import hashlib
def main():
    message = "Alicia -> Bob 15 pavos"
    nonce, hash_result = find_nonce(message)
    print(f"Nonce encontrado: {nonce}")
    print(f"Hash resultante: {hash_result}")

def find_nonce(message, prefix='00000000'):
    nonce = 0
    while True:
        data = f"{nonce}{message}".encode('utf-8')
        hash_result = hashlib.sha256(data).hexdigest()
        if hash_result.startswith(prefix):
            return nonce, hash_result
        nonce += 1

if __name__ == "__main__":
    main()