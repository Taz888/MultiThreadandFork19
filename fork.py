import multiprocessing
import random
import time

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def search_in_array(array, target, start, end, result):
    for i in range(start, end):
        if array[i] == target:
            result.put(i)
            return

def parallel_search(array, target, num_processes=1):
    result = multiprocessing.Queue()

    chunk_size = len(array) // num_processes
    processes = []

    start_time = time.time()

    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size if i < num_processes - 1 else len(array)
        process = multiprocessing.Process(target=search_in_array, args=(array, target, start, end, result))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    while not result.empty():
        index = result.get()
        print(f"Target found at index: {index}")

    print(f"Time elapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    array_size = 100000
    target_number = random.randint(0, 1000)
    array = generate_random_array(array_size)
    
    print(f"Searching for target number: {target_number}")
    parallel_search(array, target_number)
