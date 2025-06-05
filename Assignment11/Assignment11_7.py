def pattern(n, i=1):
    if i > n:
        return 
    print("* " * i)
    pattern(n, i + 1)


def main():
    no = int(input("Enter Number : "))
    result = pattern(no)
      
if __name__ == "__main__":
    main()