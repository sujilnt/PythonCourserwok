from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input


class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        inputText="Select the queries and type according to left side of option queries displayed below \n 1) d - display the items in the warehouse , \n 2) a - add an item to the warehouse \n 3) sy - setting the book according to publication year \n 4) si - subsets of books stored in the specified ISBN \n 5) ol- status of all books with a specified ISBN to on loan \n 6) nl-  status of all books with a specified ISBN to not on loan.\n "
        item = input(inputText).strip()
        if item=='d':
            print("The warehouse contains these books :", warehouse.list_contents())
        if item == 'a' :
            additem = input("Add an item to the warehouse, Enter the input in the form of , a,author,ISBN,title,year :\n").strip()
            warehouse.store(self.name, additem)
        if item == "sy":
            retrieveBook = input("Retreiving the book according according to published data, Enter the input in the form of, sy,year1,year2 :\n").strip()
            warehouse.retrieveBookYOP(self.name, retrieveBook)
        if item == "si":
            retrieveISBN = input("Retreiving the book according according to ISBN, Enter the input in the form of, si,ISBN :\n").strip()
            warehouse.retrieveISBN(self.name, retrieveISBN)
        if item == "ol":
            retrieveISBN = input("Set the status of all books with a specified ISBN to on loan, Enter the input in the form of, ol,ISBN  :\n").strip()
            warehouse.onLoan(self.name, retrieveISBN)
        if item == "nl":
            retrieveISBN = input("Set the status of all books with a specified ISBN to not on loan, Enter the input in the form of, nl,ISBN  :\n").strip()
            warehouse.notOnLoan(self.name, retrieveISBN)

