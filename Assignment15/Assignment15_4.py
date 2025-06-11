import sys

def compare_files(file1, file2):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            fobj1 = f1.read()
            fobj2 = f2.read()

            if (fobj1 == fobj2):
                print("Success: content from Both Files are Matching")
            else:
                print("Failure: Content from Files are not matching")

    except FileNotFoundError:
        print("One File or Both the Files are not Matching")
    except Exception as e:
        print(f"Error occured is : {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: Python compare_files.py text1.py text2.py")
    else:
        compare_files(sys.argv[1], sys.argv[2])