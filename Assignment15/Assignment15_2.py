'''
def main():
    print("Enter file name that you want to create: ")
    FileName = input()

    fobj = open(FileName, "w")

    print("Enter the data you want to write: ")
    data = input()
    fobj.write(data)

    fobj.close

if __name__ == "__main__":
    main()

                                            '''

import os 

def main():
    print("Enter file Name that you want to read: ")
    FileName = input()

    ret = os.path.exists(FileName)

    if (ret == True):
        print("File is Available")
        fobj = open(FileName, "r")
        data = fobj.read()
        print("Data from file is : ", data)
        fobj.close()
    else:
        print("File is Not available")

if __name__ == "__main__":
    main()
