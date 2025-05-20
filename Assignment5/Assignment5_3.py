def checkeligible():

    age = int(input("Enter age of candidate : "))

    if (age >= 18):
        print("Candidate is eligible for Voting")
    else:
        print("Candidate not eligible for voting") 


if __name__ == "__main__":
    checkeligible()