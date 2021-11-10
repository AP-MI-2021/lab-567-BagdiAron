from Domain.book2 import *


def reducere_pret(lst_vanzari):
    result = []
    for vanzare in lst_vanzari:
        if get_reducere(vanzare)=="silver":
            pret_nou = get_pret(vanzare) - (5 / 100) * get_pret(vanzare)
            result.append(create_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                pret_nou,
                get_reducere(vanzare),
            ))
        elif get_reducere(vanzare)=="gold":
            pret_nou = get_pret(vanzare) - (10 / 100) * get_pret(vanzare)
            result.append(create_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                pret_nou,
                get_reducere(vanzare),
            ))
        else:
            result.append(vanzare)

    return result