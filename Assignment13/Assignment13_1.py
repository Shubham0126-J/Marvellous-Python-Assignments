class BookStore:
    NoOfBooks = 0

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}.No of Books : {BookStore.NoOfBooks}")

Obj1 = BookStore("Linux System programming","Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming"," Dennis Ritchie")
Obj2.Display() 