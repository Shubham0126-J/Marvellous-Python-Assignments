import time
import threading
import multiprocessing

def compute_sum():
    return sum(range(1, 10000001))

def thread_sum():
    compute_sum()

def process_sum():
    compute_sum()

def main():
    # Normal function 
    start = time.time()
    compute_sum()
    end = time.time()
    print(f"normal execution time: {end - start} seconds")

    # Threading execution
    start = time.time()
    t = threading.Thread(target = thread_sum)
    t.start ()
    t.join ()
    end = time.time()
    print(f"Threading execution time : {end - start} Seconds") 

    # multiprocessing execution
    start = time.time()
    p = multiprocessing.Process(target = process_sum)
    p.start()
    p.join()
    end = time.time()
    print(f"Multiprocessingexecution time : {end - start} seconds")

if __name__ == "__main__":
    main()