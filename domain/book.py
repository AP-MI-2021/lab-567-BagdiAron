#Adăugare / ștergere / modificare vânzare: se efectuează pe bază de număr de vânzare / ID. O vânzare conține:
# ID, titlu carte, gen carte, preț, tip reducere client (none, silver, gold).


def add_new_books(id: int,title: str,gen: str, price: float,sale: str):
    book = {
        "id": id,
        "title": title,
        "gen": gen,
        "price": price,
        "sale": sale
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


def get_sale(book):
    return book["sale"]

def get_book_string(book):
    return f'cartea cu id-ul {get_id(book)},cu numele {get_title(book)},si genul {get_gen(book)},avand pretul {get_price(book)},si reducerea {get_sale(book)}'