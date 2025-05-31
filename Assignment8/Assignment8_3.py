import threading

def even_sum(data):
    total = 0
    for i in data:
        if i % 2 == 0:
            total += i
    print(f"{threading.current_thread().name} : Sum of Even number : {total}")
        
def odd_sum(data):
    total = 0
    for i in data:
        if i % 2 != 0:
            total += i
    print(f"{threading.current_thread().name } : Sum of Odd number : {total}")



def main():
    no = int(input("Enter number of elements: "))

    data = []

    for i in range(no):
        num = int(input(f"Enter number {i + 1 } : "))
        data.append(num)
        
    even_thread = threading.Thread (target = even_sum, args=(data,), name="Evenlist")
    odd_thread = threading.Thread (target = odd_sum, args=(data,), name = "Oddlist")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()