from domain.book import *
from logic.crud import *
from logic.gen_change import get_new_gen
from logic.discount_type import get_discount


def run_ui2(books):
    strr = input("sirul de comenzi introduse este ")
    for index in strr.split(';'):
        var = index.split(',')
        match var[0]:
            case "add":
                if (len(var)) >= 6:
                    create(books,int(var[1]),str(var[2]),str(var[3]),float(var[4]),str(var[5]))
            case "show":
                if (len(var)) >= 2:
                    print(get_book_string((books[int(var[1]) - 1])))
            case "remove":
                if(len(var)) > 2:
                    delete(books,int(var[1]))
            case "update":
                if(len(var)) > 2:
                    new_book=add_new_books(int(var[1]),str(var[2]),str(var[3]),float(var[4]),str(var[5]))
                    books=update(books,new_book)
            case "change":
                if(len(var)) > 2:
                    books=get_new_gen(books,var[1],var[2])
            case "discount":
                    books = get_discount(books)
            case"showall":
                print(books)