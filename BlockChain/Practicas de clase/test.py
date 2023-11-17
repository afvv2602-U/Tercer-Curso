import hashlib
import multiprocessing

def search_nonce(starting_value, increment_by, mensaje, prefix='00000000'):
    current_value = starting_value
    while True:
        combined_string = str(current_value).encode('utf-8') + mensaje
        hashed_value = hashlib.sha256(combined_string).hexdigest()

        if hashed_value.startswith(prefix):
            return current_value, hashed_value

        current_value += increment_by

def run_parallel_search(process_count):
    mensaje = "Alicia -> Bob 15 pavos".encode('utf-8')
    with multiprocessing.Pool(process_count) as pool:
        results = pool.starmap(search_nonce, [(idx, process_count, mensaje) for idx in range(process_count)])
        
        # Retornar el resultado del primer proceso que termine
        for found_nonce, hash_result in results:
            if hash_result.startswith('00000000'):
                return found_nonce, hash_result

if __name__ == "__main__":
    total_processes = multiprocessing.cpu_count()  # Usar todos los núcleos disponibles.
    found_nonce, hash_result = run_parallel_search(total_processes)
    print(f"Nonce: {found_nonce}")
    print(f"Hash: {hash_result}")
