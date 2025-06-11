'''
import os
def main():
    print("Enter file Name you want to create")
    FileName = input()

    ret = os.path.exists(FileName)

    if (ret == True):
        print("File is already available ")
    else :
        fobj = open(FileName,"w")
        print("Enter Data you want to Write")
        data = input()
        fobj.write(data)
        print("Data from file is : ", data)
    
        fobj.close()

if __name__ =="__main__":
    main()
                                        '''


import sys

def copy_file():
    if len(sys.argv)!= 2:
        print("usage: Python filename.py <source_file>")
        return

    source_file = sys.argv[1]
    target_file = "Demo.txt"

    try:
        with open(source_file, "r")as src:
            content = src.read()

        with open(target_file, "w") as tgt:
            tgt.write(content)

        print(f"Contents copied from {source_file} to {target_file} successfully")

    except FileNotFoundError:
        print(f"Error: The file{source_File} does not exist.")
    except Exception as e:
        print(f"An error occured: {e}")

copy_file()