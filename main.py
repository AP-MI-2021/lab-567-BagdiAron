# D, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).


from domain.book import get_new_book, get_id
from logic.crud import create
from domain.book2 import *


def main():
    books = []
    books = create(books, 1,'poezii', 'romatic', 45, 'gold')

if __name__=='__main__':
    main()