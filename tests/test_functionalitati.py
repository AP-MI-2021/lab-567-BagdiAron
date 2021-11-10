from UI.ui import handle_undo, handle_redo, handle_new_list
from tests.tests import get_data
from Logic.crud import delete, create, update, read
from Logic.gen_change import *
from Logic.nr_titluri import *
from Logic.ordonare import *
from Logic.pret_min import *
from Logic.discount_type import *
from UI.clc import *


def test_reducere_pret():
    lista = get_data()
    lista = reducere_pret(lista)
    assert get_pret(lista[0]) == 100
    assert get_pret(lista[1]) == 66.5
    assert get_pret(lista[2]) == 18.0


def test_min_price_by_gen():
    lista = get_data()
    preturi_minime = min_price_by_gen(lista)
    assert preturi_minime[0] == 48


def test_ordonare():
    lista = get_data()
    new_list = ordonare_vanzari_pret(lista)
    assert get_id(new_list[0]) == 3
    assert get_id(new_list[1]) == 5
    assert get_id(new_list[2]) == 2


def test_modificare_gen_dupa_titlu():
    lista = get_data()
    lista_noua=modificare_gen_dupa_titlu(lista,'Ana','gen_nou')
    assert get_gen(lista[2]) != get_gen(lista_noua[2])


def test_undo():
    lista=get_data()
    current_version = 0
    list_versions = [lista]
    lista_noua = delete(lista,1)
    list_versions,current_version=handle_new_list(list_versions,current_version,lista_noua)
    assert current_version == 1
    assert len(list_versions)==2
    assert len(list_versions[current_version])==3
    lista_noua,current_version=handle_undo(list_versions,current_version)
    assert current_version == 0
    assert len(lista_noua)==4


def test_redo():
    lista=get_data()
    current_version = 0
    list_versions = [lista]
    lista_noua = delete(lista,1)
    list_versions,current_version=handle_new_list(list_versions,current_version,lista_noua)
    assert current_version == 1
    assert len(list_versions)==2
    assert len(list_versions[current_version])==3
    lista_noua,current_version=handle_undo(list_versions,current_version)
    assert current_version == 0
    assert len(lista_noua)==4
    lista_noua, current_version = handle_redo(list_versions, current_version)
    assert current_version == 1
    assert len(list_versions) == 2
    assert len(list_versions[current_version]) == 3


def test_all():
    test_reducere_pret()
    test_min_price_by_gen()
    test_ordonare()
    test_modificare_gen_dupa_titlu()
    test_undo()
    test_redo()
test_all()