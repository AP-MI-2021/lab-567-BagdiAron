# D, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
def get_new_book (id: int, title: str,gen: str, price: float,discout: str):
    return [id,title,gen,price,discount]


def get_id(book):
    return bookp[o]


def get_title(book):
    return book[1]


def get_gen(book):
    return book[2]


def get_price(book):
    return book[3]


def get_discount(book):
    return book[4]

def to_string(book):
    return "id: {}, nume: {}, gen: {}, pret: {}, discount: {}".format(
        get_id(book),
        get_nume(book),
        get_clasa(book),
        get_pret(book),
        get_checkin(book),

    )