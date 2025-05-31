import threading

def count_small(s):
    count = sum(1 for c in s if c.islower())
    print(f"Thread Name: {threading.current_thread().name}, ID: {threading.get_ident()}, Small letters: {count}")

def count_capital(s):
    count = sum(1 for c in s if c.isupper())
    print(f"Thread Name: {threading.current_thread().name}, ID: {threading.get_ident()}, Capital letters : {count}")


def count_digits(s):
    count = sum(1 for c in s if c.isdigit())
    print(f"Thread Name: {threading.current_thread().name}, ID: {threading.get_ident()}, Digits : {count}")


def main():
    string = input("Enter a string : ")

    t1 = threading.Thread(target = count_small, args=(string,), name="Small")
    t2 = threading.Thread(target = count_capital, args=(string,), name="Capital")
    t3 = threading.Thread(target = count_digits, args=(string,), name='Digits')

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()