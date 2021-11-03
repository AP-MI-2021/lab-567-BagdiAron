from domain.book import *

def get_discount(list: list):
    result_list = []
    for book in list:
        #if get_sale(book) is not 'gold' or get_sale(book) is not 'silver' or get_sale(book) is not 'none':
         #   raise ValueError('nu ati verificat bine tipul de reducere')
        if get_sale(book) == 'silver':
            new_price = get_price(book) - get_price(book)/20
            result_list.append(
                add_new_books(
                    get_id(book),
                    get_title(book),
                    get_gen(book),
                    new_price,
                    get_sale(book)
            ))
        elif get_sale(book) == 'gold':
            new_price = get_price(book) - get_price(book)/10
            result_list.append(
                add_new_books(
                    get_id(book),
                    get_title(book),
                    get_gen(book),
                    new_price,
                    get_sale(book)
                ))
        else:
            result_list.append(book)

    return result_list