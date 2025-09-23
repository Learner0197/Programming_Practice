class Book:
    def __init__(self,bookid,title,author,status):
        self.bookid=bookid
        self.title=title
        self.author=author
        self.status=status
    def isavailable(self):
        if self.status=="Issued":
            return False
        elif self.status=="Available":
            return True
     def setstatus(self,T):
         if


class Member:
    bookissued=[]
    def __init__(self,memid,name,bookissued):
        self.memid=memid
        self.name=name
        self.bookissued=bookissued
    def issue(self.bookid):


class Library:
    b1=Book(1,"Business Analytics","Andrew Ng","Issued")
    print("Hello")