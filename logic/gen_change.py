from domain.book import *

def get_new_gen(list: list, str1: str, str2: str):
    if str1 == '':
        raise   ValueError('nu a fost introdus un nume de carte')

    result_list = []
    for book in list:
        if str1 == get_title(book):
            new_gen = str2
            result_list.append(add_new_books(
                get_id(book),
                get_title(book),
                new_gen,
                get_price(book),
                get_sale(book)
            ))
        else:
            result_list.append(book)
    return result_list