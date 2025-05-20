def palindrome(s):
   return s == s[::-1]

def main():

   text = input ("Enter a string : ")

   if palindrome(text):
      print(f"{text} is palindrome")
   else:
      print(f"{text} is not palindrome")

if __name__ == "__main__":
   main()