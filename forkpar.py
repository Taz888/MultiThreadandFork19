import random
import time
import multiprocessing

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def search_in_chunk(args):
    chunk, target = args
    result = []
    for i, num in enumerate(chunk):
        if num == target:
            result.append(i)
    return result

def parallel_search(array, target, num_processes=4):
    pool = multiprocessing.Pool(processes=num_processes)

    chunk_size = len(array) // num_processes
    chunks = [(array[i * chunk_size:(i + 1) * chunk_size], target) for i in range(num_processes)]

    start_time = time.time()

    results = pool.map(search_in_chunk, chunks)
    pool.close()
    pool.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    result_indices = [index for sublist in results for index in sublist]

    for index in result_indices:
        print(f"Target found at index: {index}")

    print(f"Time elapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    array_size = 1000000
    target_number = random.randint(0, 1000)
    array = generate_random_array(array_size)
    
    print(f"Searching for target number: {target_number}")
    parallel_search(array, target_number)
