import threading
import random
import time

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def search_in_array(array, target, start, end, result):
    for i in range(start, end):
        if array[i] == target:
            result.append(i)

def parallel_search(array, target, num_threads=1):
    result = []
    chunk_size = len(array) // num_threads
    threads = []

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(array)
        thread = threading.Thread(target=search_in_array, args=(array, target, start, end, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    for index in result:
        print(f"Target found at index: {index}")

    print(f"Time elapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    array_size = 100000
    target_number = random.randint(0, 1000)
    array = generate_random_array(array_size)
    
    print(f"Searching for target number: {target_number}")
    parallel_search(array, target_number)
