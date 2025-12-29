import time
from binarySearch import binary_search_iterative, binary_search_recursive

def measure_search(data, target_nim):
    start = time.perf_counter()
    result_iter = binary_search_iterative(data, target_nim)
    time_iter = time.perf_counter() - start

    start = time.perf_counter()
    result_rec = binary_search_recursive(data, target_nim, 0, len(data)-1)
    time_rec = time.perf_counter() - start

    return result_iter, time_iter, result_rec, time_rec

def measure_search_optimize(data, target_nim):
    start = time.perf_counter()
    result_iter_opt = binary_search_iterative(data, target_nim) 
    time_iter_opt = time.perf_counter() - start

    start = time.perf_counter()
    result_rec_opt = binary_search_recursive(data, target_nim, 0, len(data)-1) 
    time_rec_opt = time.perf_counter() - start

    return result_iter_opt, time_iter_opt, result_rec_opt, time_rec_opt