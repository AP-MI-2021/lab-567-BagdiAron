# D, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).
def get_new_book (id: int, title: str,gen: str, price: float,discout: str):
    book ={
        "id": id,
        "title": title,
        "gen": gen,
        "price": price,
        "discount": discout
    }
    return book


def get_id(book):
    return book["id"]


def get_title(book):
    return book["title"]


def get_gen(book):
    return book["gen"]


def get_price(book):
    return book["price"]


def get_discount(book):
    return book["discount"]

def to_string(book):
    return "id: {}, nume: {}, gen: {}, pret: {}, discount: {}".format(
        get_id(book),
        get_nume(book),
        get_clasa(book),
        get_pret(book),
        get_checkin(book),

    )