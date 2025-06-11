import sys

def count_string(FileName, search_string):
    try:
        with open(FileName, "r")as file:
            fobj = file.read()
            count = fobj.count(search_string)
            print(f"The word {search_string} appears {count} times in file")

    except FileNotFoundError:
        print("Error: Entered File Not available")
    except Exception as e:
        print(f"Error occured is : {e}")


def main():
    FileName = input("Enter the File Name : ")
    search_string = input("Enter the string to Search: ")

    count_string(FileName, search_string)


if __name__ == "__main__":
    main()
