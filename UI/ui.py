from domain.book import *
from logic.crud import *
from logic.gen_change import get_new_gen
from logic.discount_type import get_discount


def handle_add(books):
    try:
        id_book = int(input('Dati id-ul cartii: '))
        title = input('Dati numele cartii: ')
        gen = input('Dati genul cartii: ')
        price = float(input('Dati pretul cartii: '))
        sale = input("dati tipul de reducere aplicata cartii")
        return create(books, id_book, title, gen, price, sale)
    except ValueError as ve:
        print('Eroare:', ve)

    return prajituri

def handle_show_all(books):
    for book in books:
        print(get_book_string(book))


def handle_show_details(books):
    id_book = int(input('Dati id-ul cartii pentru care doriti detalii: '))
    book = read(books, id_book)
    print(f'title: {get_title(book)}')
    print(f'gen: {get_gen(book)}')
    print(f'pret: {get_price(book)}')
    print(f'reducere: {get_sale(book)}')



def handle_update(books):
    try:
        id_book = int(input('Dati id-ul cartii care se actualizeaza: '))
        title = input('Dati noul nume al prajiturii: ')
        gen = input('Dati noua descriere prajiturii: ')
        price = float(input('Dati noul pret al prajiturii: '))
        sale = int(input('Dati noua reducere: '))
        return update(books, add_new_books(id_book, title, gen, price, sale))
    except ValueError as ve:
        print('Eroare:', ve)


def handle_delete(books):
    try:
        id_book = int(input('Dati id-ul cartii care se va sterge: '))
        prajituri = delete(books, id_book)
        print('Stergerea a fost efectuata cu succes.')
        return books
    except ValueError as ve:
        print('Eroare:', ve)

    return books


def handle_gen_change(books):

    try:
        str1 = input("numele cartii cerut ")
        str2 = input("genul care va fi actualizat: ")
        books = get_new_gen(books,str1,str2)
        print ('genul a fost schimbat cu succes')
    except  ValueError as ve:
        print('Eroare', ve)

    return books

def handle_discount_applied(books):

    try:
        books = get_discount(books)
    except ValueError as ve:
        print("Eroare", ve)
    return books

def handle_crud(books):
    print('1. Adaugare')
    print('2. Modificare')
    print('3. Stergere')
    print('a. Afisare')
    print('d. Detalii prajitura')
    # print('b. Revenire')

    optiune = input('Optiunea aleasa: ')
    if optiune == '1':
        books = handle_add(books)
    elif optiune == '2':
        books = handle_update(books)
    elif optiune == '3':
        books = handle_delete(books)
    elif optiune == 'a':
        handle_show_all(books)
    elif optiune == 'd':
        handle_show_details(books)
    # elif optiune == 'b':
    #     break
    else:
        print('Optiune invalida.')
    return books

def show_menu():
    print('1. CRUD')
    print('2. schimbare gen anumitor carti cu un gen dat.')
    print('3. aplicare reducere')
    print('z. Undo.')
    print('y. Redo.')
    print('x. Exit')


def handle_new_list(list_versions, current_version, books):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(books)
    current_version += 1
    return list_versions, current_version


def run_ui(books):

    list_versions = [books]
    current_version = 0

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            books = handle_crud(books)
            list_versions, current_version = handle_new_list(list_versions, current_version, books)
        elif optiune == '2':
            books = handle_gen_change(books)
            list_versions, current_version = handle_new_list(list_versions, current_version, books)
        elif optiune == '3':
            books = handle_discount_applied(books)
            list_versions, current_version = handle_new_list(list_versions, current_version, books)
        elif optiune == 'z':
            books, current_version = handle_undo(list_versions, current_version)
        elif optiune == 'y':
            books, current_version = handle_redo(list_versions, current_version)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return books