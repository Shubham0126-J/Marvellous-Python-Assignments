import threading

def threadone():
    for i in range(1, 50+1):
        print(i)

def threadtwo():
    for i in range(50,0,-1):
        print(i)

def main():
    t1 = threading.Thread(target = threadone, name = "thread1")
    t2 = threading.Thread(target = threadtwo, name = "thread2")

    t1.start()
    t1.join()

    print("Schedule thread2")
    
    t2.start()
    t2.join()

if __name__ =="__main__":
    main()