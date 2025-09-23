import locale


class Book:
    def __init__(self,bookid,title,author):
        self.bookid=bookid
        self.title=title
        self.author=author
        self.status= "Available"

class Member:
    def __init__(self, memID, memName):
        self.memID = memID
        self.memName = memName
        self.issuedBooks = []

class libraryOps:
    def __init__(self):
        self.lib = {}
        self.mem = {}

    def addBook(self, bookID, title, author):
        self.lib[bookID] = Book(bookID, title, author)

    def displayBooks(self):
        return self.lib

    def issueBook(self, memID, memName):
        if


