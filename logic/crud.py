from domain.book import add_new_books, get_id


def create(list_books: list,id: int,title: str,gen: str, price: float,sale: str):
    carte = add_new_books(id,title,gen,price,sale)
    list_books.append(carte)
    return list_books


def read(list_books: list, id_prajitura:int = None):
    book_found = None
    if id_prajitura is None:
        return list_books
    for book in list_books:
        if get_id(book) == id_prajitura:
            book_found = book
    return book_found

def update(list_books: list, new_book):
    result_list = []

    for book in list_books:
        if get_id(book) == get_id(new_book):
            result_list.append(new_book)
        else:
            result_list.append(book)
    return result_list

def delete (list_books: list, id_prajitura: int):
    result_list = []

    for book in list_books:
        if get_id(book) != id_prajitura:
            result_list.append(book)

    return result_list