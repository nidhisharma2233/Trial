class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
class bookcollection:
    def __init__(self):
        self.list1=[]

    def add_book(self,var):
        self.list1.append(var)

    def display(self):
        print("available books in laibrary:")
        for idk,i in enumerate(self.list1,1):
            print(idk,i.title,i.author)

    def issue(self,title):
        if title not in self.list1:
            print("this book is not available in laibrary\n")
        else:

            print("book is issue successfully\n")

    def Return(self,title):
        self.title=title
        print(f"book'{self.title}'return successfully\n")

book1=Book('artificial intelligency','F. Scott Fitzgerald')
book2=Book('c language', 'l. Scott Fitzgerald')
book3=Book('python', 'A. Scott Fitzgerald')

lab=bookcollection()
lab.add_book(book1)
lab.add_book(book2)
lab.add_book(book3)

lab.display()
lab.issue('artificial intelligency')
lab.display()
lab.Return('artificial intelligency')








