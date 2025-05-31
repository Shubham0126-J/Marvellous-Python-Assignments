import threading 

def print_even():
    for i in range (1, 11):
        print(f"{threading.current_thread().name} : { i * 2 }")

def print_odd():
    for i in range (10):
        print(f"{threading.current_thread().name} : { i * 2 + 1}")

def main():
    even_thread = threading.Thread(target = print_even, name = "Even")
    odd_thread = threading.Thread(target = print_odd, name = "Odd")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()