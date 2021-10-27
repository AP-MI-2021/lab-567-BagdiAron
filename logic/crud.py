import domain.book
import domain.book2

def create(lst_book, id, title, gen, price, discount):
    book = domain.book.get_new_book(id, title, gen, price, discount)
    return lst_book + [book]


def read(lst_book, id_book = None):
    book_found = None
    for book in lst_book:
        if Domain.book.get_id(librarie) == id_book:
            librarie_cu_id = librarie
    if book_found:
        return book_found
    return lst_book


def update(lst_book, new_book):
    new_books = []
    for book in lst_book:
        if domain.book.get_id(book) != domain.book.get_id(new_book):
            new_books.append(new_book)
        else:
            new_books.append(book)

    return new_books


def delete(lst_book, id_book):
    new_book = []
    for book in lst_book:
        if domain.book.get_id(book) != id_book:
            new_librarie.append(book)
    return new_book