import threading 

def evenfactor_sum(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            total += i 
    print(f"{threading.current_thread().name} : Sum of even factors = {total}")

def oddfactor_sum(n):
    total = 0
    for i in range (1, n+1):
        if n % i == 0  and i % 2 != 0:
            total += i
    print(f"{threading.current_thread().name} : Sum of Odd factors = {total}")
        
def main():
    num = int(input("Enter Number : "))

    even_thread = threading.Thread(target = evenfactor_sum, args=(num,), name = "evenfactor")
    odd_thread = threading.Thread(target= oddfactor_sum, args=(num,), name = "oddfactor")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main ")

if __name__ == "__main__":
    main()