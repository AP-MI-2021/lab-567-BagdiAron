from domain.book import *
from logic.crud import create,read,update

def get_data():
    return[
        add_new_books(1,'c1','d1',5,'s1'),
        add_new_books(2,'c2','d2',10,'s2'),
        add_new_books(3,'c3','d3',15,'s3'),
        add_new_books(4,'c4','d4',20,'s4'),
        add_new_books(5,'c5','d5',25,'s5')
    ]


def test_create():
    list = get_data()
    new_book = add_new_books(6,'c6','d6',25,'s6')
    new_list = create(list,6,'c6','d6',25,'s6')
    assert len(new_list) == len(list)
    assert new_book in new_list


def test_read():
    list = get_data()
    random_book = list[2]
    assert read(list,get_id(random_book)) == random_book
    assert read(list,None) ==  list


def test_update():
    list = get_data()
    new_book = add_new_books(5,'c6','d6',25,'s6')
    new_list = update(list,new_book)
    assert len(new_list) == len(list)
    assert new_book in new_list

def test_crud():
    test_create()
    test_read()
    test_update()
