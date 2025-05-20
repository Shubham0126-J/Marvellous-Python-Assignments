def main():
    
    char = input("Enter a lowercase characher : ")

    vowel = {"a", "e", "i", "o", "u"}

    if len(char) == 1 and char.isalpha():
        if char.lower() in vowel :
            print("It is vowel ")
        else :
            print("It is consonent")
    else :
        print("Invalid Entry - Enter a character")

    

if __name__ == "__main__":
    main()