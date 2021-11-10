from Domain.book import *
from Logic.crud import *
from Logic.gen_change import get_new_gen
from Logic.discount_type import get_discount


def run_ui2(books):
    strr = input("sirul de comenzi introduse este ")
    for index in strr.split(';'):
        var = index.split(',')
        match var[0]:
            case "add":
                if (len(var)) >= 6:
                    try:
                        create(books,int(var[1]),str(var[2]),str(var[3]),float(var[4]),str(var[5]))
                    except ValueError as ve :
                        print("Eroare", ve)
            case "show":
                if (len(var)) >= 2:
                    try:
                        print(get_book_string((books[int(var[1]) - 1])))
                    except ValueError as ve:
                        print("Eroare", ve)
            case "remove":
                if(len(var)) > 2:
                    try:
                        delete(books,int(var[1]))
                    except ValueError as ve:
                        print("Eroare", ve)
            case "update":
                if(len(var)) > 2:
                    try:
                        new_book=add_new_books(int(var[1]),str(var[2]),str(var[3]),float(var[4]),str(var[5]))
                        books=update(books,new_book)
                    except ValueError as ve:
                        print("Eroare", ve)
            case "change":
                if(len(var)) > 2:
                    try:
                        books=get_new_gen(books,var[1],var[2])
                    except ValueError as ve:
                        print("Eroare", ve)
            case "discount":
                try:
                    books = get_discount(books)
                except ValueError as ve:
                    print("Eroare",  ve)
            case"showall":
                print(books)