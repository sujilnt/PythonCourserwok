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

    def take(self, name, item):
        self.contents.remove(item)
        print("{0} took the {1}.".format(name, item))

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

    def retrieveBook(self,name, item):
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
                        print(val)
        print("\n")
        print("The books name published between the  years =>",fromyear, toyear,"are :- " ,books)
        print("\n")
