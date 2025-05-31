import threading
import time

def threadone():
    for i in range(1, 6):
        print(i)

def threadtwo():
    for i in range(1, 6):
        print(i)

def threadthree():
    for i in range(1, 6):
        print(i)

def main():
    t1 = threading.Thread(target = threadone, name = "Thread1")
    t2 = threading.Thread(target = threadtwo, name = "Thread2")
    t3 = threading.Thread(target = threadthree, name = "Thread3")

    t1.start()
    t1.join()

    time.sleep(1)

    t2.start()
    t2.join()

    time.sleep(2)

    t3.start()
    t3.join()

if __name__ == "__main__":
    main()