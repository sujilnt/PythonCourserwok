from __future__ import print_function
import pprint
pp = pprint.PrettyPrinter(indent=2)

class Warehouse(object):
    def __init__(self):
        self.contents = [{"BookId":1,
       "bookAuthor": "Enid Blyton",
       "bookName": "The Famous Five",
       "bookIsbn": 9332549532,
       "YOP": 2001,
       "loan": "yes"
       },
      {"BookId":2,
       "bookAuthor": "Savitha Hosamanne",
       "bookName": "Erupt Of Joy",
       "bookIsbn": 9332549533,
       "YOP": 2001,
       "loan": "no"
       },
      {"BookId":3,
       "bookAuthor": "Enid Blyton",
       "bookName": "Five Find Outers",
       "bookIsbn": 9332549534,
       "YOP": 2014,
       "loan": "no"
       }
      ]

    def list_contents(self):
        books=[]
        pp.pprint(self.contents)
        for val in self.contents:
            books.append(val['bookName'])
        return books

    def onLoan(self, name, item):
        books = []
        item = item.split("ol,")
        for i in item:
            if (len(i) > 1):
                for val in self.contents:
                    if (str(val["bookIsbn"]) == i):
                        pp.pprint(val)
                        load={"loan":"yes"}
                        val.update(load)
                        books.append(val["bookName"])
        if (len(books) < 1):
            print("no books on this ISBN In the library")
        print("This particular book is set to the loan with this ISBN ", books)

    def notOnLoan(self, name, item):
        books = []
        item = item.split("nl,")
        for i in item:
            if (len(i) > 1):
                for val in self.contents:
                    if (str(val["bookIsbn"]) == i):
                        pp.pprint(val)
                        load = {"loan": "no"}
                        val.update(load)
                        books.append(val["bookName"])
        if (len(books) < 1):
            print("no books on this ISBN In the library")
        print("This particular book is set no to the loan with this ISBN ", books)

    def store(self, name, item):
        bookObj=["bookAuthor","bookIsbn","bookName","YOP"]
        obj={}
        books=[]
        item=item.split('a,')
        for i in item:
            item=i.split(",")
            obj = dict(zip(bookObj, item))
            obj["BookId"]=len(self.contents)
            obj["loan"]="no"
        print("coverting and adding your book to Database", obj)
        self.contents.append(obj)
        pp.pprint(self.contents)
        for val in self.contents:
            books.append(val['bookName'])

        print("The new Added on the list",books)

    def retrieveISBN(self,name,item):
        books=[]
        item=item.split("si,")
        for i in item:
            if(len(i)>1):
                for val in self.contents:
                    if(str(val["bookIsbn"])== i):
                        pp.pprint(val)
                        books.append(val["bookName"])
        print ("The book Names with same ISBN ", books)



    def retrieveBookYOP(self,name, item):
        books=[]
        fromyear=0
        toyear=1
        item = item.split("sy,")
        for i in item:
            if(len(i)>0):
                i = i.split(",")
                fromyear=int(i[0])
                toyear=int(i[1])

                for val in self.contents:
                    if(val["YOP"]<=int(i[1]) and val["YOP"]>=int(i[0])):
                        books.append(val["bookName"])
                        pp.pprint(val)
        print("\n")
        if(len(books)< 1 ):
            print("no books.... are Published between these years")
        print("The books name published between the  years =>",fromyear, toyear,"are :- " ,books)
        print("\n")
