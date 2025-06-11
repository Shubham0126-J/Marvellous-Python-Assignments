
import os 

def main():
    print("Enter the file Name that you want to check")
    FileName = input()

    ret = os.path.exists(FileName)

    if (ret == True):
        print("File is present in current direcory")
    else:
        print("File is not present")


if __name__ == "__main__":
    main()