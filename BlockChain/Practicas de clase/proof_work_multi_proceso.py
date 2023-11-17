import hashlib
import multiprocessing

def search_nonce(starting_value, increment_by, transaction_string, target_prefix='00000000', queue=None):
    """
    Busca un nonce que, cuando se añade al principio de un string, produce un hash que comienza con un prefijo específico.
    
    :param starting_value: El valor inicial desde donde comenzar la búsqueda del nonce.
    :param increment_by: El valor para incrementar el nonce en cada iteración.
    :param transaction_string: El string al que se le añadirá el nonce para producir el hash.
    :param target_prefix: El prefijo que debe tener el hash resultante.
    :param queue: Una cola donde se colocará el resultado cuando se encuentre el nonce.
    
    :return: Retorna el nonce y el hash resultante.
    """
    current_value = starting_value
    while True:
        combined_string = f"{current_value}{transaction_string}".encode('utf-8')
        hashed_value = hashlib.sha256(combined_string).hexdigest()
        
        if hashed_value.startswith(target_prefix):
            if queue:
                queue.put((current_value, hashed_value))
                return
            else:
                return current_value, hashed_value

        current_value += increment_by

def run_parallel_search(process_count):
    """
    Inicia múltiples procesos para buscar el nonce en paralelo.
    
    :param process_count: Número de procesos que se deben iniciar.
    
    :return: Retorna el nonce y el hash resultante encontrados.
    """
    transaction_string = "Alicia -> Bob 15 pavos"
    results_queue = multiprocessing.Queue()
    all_processes = []

    # Iniciar múltiples procesos, cada uno buscando el nonce con diferentes valores iniciales.
    for idx in range(process_count):
        process = multiprocessing.Process(target=search_nonce, args=(idx, process_count, transaction_string, '00000000', results_queue))
        all_processes.append(process)
        process.start()

    # Esperar a que algún proceso encuentre el nonce y lo coloque en la cola.
    found_nonce, hash_result = results_queue.get()

    # Terminar todos los procesos una vez que se haya encontrado el nonce.
    for process in all_processes:
        process.terminate()

    return found_nonce, hash_result

if __name__ == "__main__":
    total_cores = multiprocessing.cpu_count()  # Obtener el número de núcleos del procesador.
    found_nonce, hash_result = run_parallel_search(total_cores)

    print(f"Nonce: {found_nonce}")
    print(f"Hash: {hash_result}")
