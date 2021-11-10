from Logic.crud import create
from tests.tests import *
from tests.test_functionalitati import *
from UI.ui import *

def main():
    lista_vanzari = []
    lista_vanzari=get_data()
    lista_vanzari = run_ui(lista_vanzari)

if __name__ == '__main__':
    test_crud()
    test_all()
    main()