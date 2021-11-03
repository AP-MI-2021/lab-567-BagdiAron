from domain.book import *
from logic.crud import *
from tests.tests import test_crud
from UI.ui import run_ui
from UI.ui2 import run_ui2

def main():
    books = []
    books = create(books, 1, 'cartea1', 'aventura', 10, 'none')
    books = create(books, 2, 'cartea2', 'drama', 12,'none')
    books = create(books, 3, 'cartea3', 'comedie', 17, 'silver')
    books = create(books, 4, 'cartea4', 'comedie', 60, 'gold')
    books = create(books, 5, 'cartea5', 'aventura :(', 21, 'gold')
    books = create(books, 6, 'cartea6', 'SF', 14, 'silver')
    books = create(books, 7, 'cartea7', 'drama', 23, 'none')
    books = run_ui2(books)

if __name__ == '__main__':
    test_crud()
    main()