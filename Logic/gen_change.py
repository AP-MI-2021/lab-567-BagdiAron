from Domain.book2 import *


def modificare_gen_dupa_titlu(lista_vanzari,titlu,gen_nou):

    if titlu== '':
        raise ValueError('Textul cautat nu poate fi gol.')
    result = []
    gasit=0
    for vanzare in lista_vanzari:
        if titlu == get_titlu(vanzare):
            gasit=1
            id_vanzare=get_id(vanzare)
            result.append(create_vanzare(
                get_id(vanzare),
                titlu,
                gen_nou,
                get_pret(vanzare),
                get_reducere(vanzare),
            ))
        else:
            result.append(vanzare)
    if gasit==0:
        raise ValueError('titlu pe care l-ati dat nu exista')

    return result
