
''' 9. Write a program which display first 10 even numbers on screen. '''

def Chknum():
    
    for i in range(1,11):
        print(i * 2 , end = "  ")


if __name__ == '__main__':
    Chknum()


def Chknum():
    
    print(list(range(2,21,2)))

if __name__ == "__main__":
    Chknum()

count = 0
num = 2

while count < 10:
    print(num)
    num += 2
    count += 1
