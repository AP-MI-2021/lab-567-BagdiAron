from Domain.book2 import *


def ordonare_vanzari_pret(lista_vanzari):
    return sorted(lista_vanzari,key=get_pret)